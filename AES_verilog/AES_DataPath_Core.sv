module AES_DataPath_Core (
    // from user
    input wire clk,
    input wire rst,
    input wire [7:0] data_in,
    // from key schedule
    input wire [7:0] round_key_delayed,
    input wire [7:0] round_key_last,
    //from inner state counter
    input wire [3:0] inner_state_counter,
    // from controller
    input wire encrypt,
    input wire rst_synch,
    input wire first_round,
    // output
    output reg [7:0] data_out
);
    wire [7:0] parallel_d_in0;
    wire [7:0] parallel_d_in1;
    wire [7:0] parallel_d_in2;
    wire [7:0] parallel_d_in3;
    wire [7:0] d_out_parallel_to_serial;
    wire en_parallel_load;
    Mix_Column_and_Parallel_to_Serial_Controller MC_PS_C (
        .inner_state_counter(inner_state_counter),
        .en_parallel_load(en_parallel_load)
    );
    reg first_round_d_1;
    reg first_round_d_2;
    reg first_round_d_3;
    reg first_round_d_4;
    always@(posedge clk)begin
        first_round_d_1 <= first_round;
        first_round_d_2 <= first_round_d_1;
        first_round_d_3 <= first_round_d_2;
        first_round_d_4 <= first_round_d_3;
    end
    Parallel_to_Serial PTS (
        .clk(clk),
        .rst(rst),
        .en_paralle(en_parallel_load && ~first_round && ~first_round_d_4),
        .serial_d_in(data_in),
        .parallel_d_in0(parallel_d_in0),
        .parallel_d_in1(parallel_d_in1),
        .parallel_d_in2(parallel_d_in2),
        .parallel_d_in3(parallel_d_in3),
        .d_out(d_out_parallel_to_serial));
    
    wire [7:0] BPU_in_data;
    assign BPU_in_data = (encrypt || first_round || first_round_d_4) ? 
                         d_out_parallel_to_serial ^ round_key_delayed :
                         d_out_parallel_to_serial;
    wire [7:0] BPU_out_data;
    assign shift_left = encrypt;
    Byte_Permutation_Unit BPU(
        .clk(clk),
        .rst(rst),
        .rst_synch(rst_synch),
        .shift_left(encrypt),
        .inner_state_counter(inner_state_counter),
        .in_byte(BPU_in_data),
        .out_byte(BPU_out_data));
    
    wire[7:0] sbox_out;
    bSbox  b_s_box(
        .A(BPU_out_data),
        .encrypt(encrypt),
        .Q(sbox_out));
    
    Mix_Column mix_column (
        .rst(rst),
        .clk(clk),
        .en(en_parallel_load),
        .encrypt(encrypt),
        .d_in(encrypt ? sbox_out : data_out),
        .d_out0(parallel_d_in0),
        .d_out1(parallel_d_in1),
        .d_out2(parallel_d_in2),
        .d_out3(parallel_d_in3)
    );
    assign data_out = sbox_out ^ round_key_last;
endmodule