module AES_DataPath_Core (
    // from user
    input wire clk,
    input wire rst,
    input wire [7:0] data_in,
    // from key schedule
    input wire [7:0] round_key_delayed,
    input wire [7:0] round_key_last,
    // from controller
    input wire en_paralle_load,
    input wire cipher,
    input wire bpu_rst_synch,
    // output
    output reg [7:0] data_out
);
    wire cipher;
    assign cipher = ~decipher;
    wire [7:0] parallel_d_in0;
    wire [7:0] parallel_d_in1;
    wire [7:0] parallel_d_in2;
    wire [7:0] parallel_d_in3;
    wire [7:0] d_out_parallel_to_serial;
    Parallel_to_Serial PTS (
        .clk(clk),
        .rst(rst),
        .en_paralle(en_paralle_load),
        .serial_d_in(data_in),
        .parallel_d_in0(parallel_d_in0),
        .parallel_d_in1(parallel_d_in1),
        .parallel_d_in2(parallel_d_in2),
        .parallel_d_in3(parallel_d_in3),
        .d_out(d_out_parallel_to_serial));
    
    wire [7:0] BPU_in_data;
    assign BPU_in_data = d_out_parallel_to_serial ^ round_key_delayed;
    wire [7:0] BPU_out_data;
    assign shift_left = ~decipher;
    Byte_Permutation_Unit BPU(
        .clk(clk),
        .rst(rst),
        .rst_synch(rst_synch),
        .shift_left(cipher),
        .in_byte(BPU_in_data),
        .out_byte(BPU_out_data));
    
    wire[7:0] sbox_out;
    bSbox  b_s_box(
        A(BPU_out_data),
        encrypt(cipher),
        Q(sbox_out));
    
    Mix_Column mix_column (
        .rst(rst),
        .clk(clk),
        .en(en),
        .d_in(sbox_out),
        .d_out0(parallel_d_in0),
        .d_out1(parallel_d_in1),
        .d_out2(parallel_d_in2),
        .d_out3(parallel_d_in3),
    );
    always @(posedge clk)begin
        data_out <= sbox_out ^ round_key_last;
    end
endmodule