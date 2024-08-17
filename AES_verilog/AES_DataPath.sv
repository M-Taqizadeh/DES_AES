module AES_DataPath (
    input wire clk,
    input wire rst,
    input wire rst_synch,
    //from user
    input wire [7:0] data_in,
    input wire [7:0] key_in,
    //from controller
    input wire en_generator,
    input wire encrypt,
    input wire first_round,
    input wire [3:0] round_counter,
    input wire read_key_in,
    input wire load_round_key,
    input wire save_round_key,
    input wire [7:0] addr_round_key_mem,
    //to controller
    output reg [3:0] inner_state_counter,
    //to user
    output reg [7:0] data_out
);
    wire [7:0] round_key_delayed;
    wire [7:0] round_key_last;
    AES_DataPath_Core aes_dp_core(
        // from user
        .clk(clk),
        .rst(rst),
        .data_in(data_in),
        // from key schedule
        .round_key_delayed(round_key_delayed),
        .round_key_last(round_key_last),
        //from inner state counter
        .inner_state_counter(inner_state_counter),
        // from controller
        .encrypt(encrypt),
        .rst_synch(rst_synch),
        .first_round(first_round),
        // output
        .data_out(data_out)
    );
    AES_DataPath_Inner_State_Counter aes_dp_isc (
        .clk(clk),
        .rst(rst),
        .rst_synch(rst_synch),
        .inner_state_counter(inner_state_counter)
    );
    AES_DataPath_Key_Schedule aes_dp_ks (
        .clk(clk),
        .rst(rst),
        .key_in(key_in),
        //from inner state counter
        .inner_state_counter(inner_state_counter),
        //from controller
        .en_generator(en_generator),

        .round_counter(round_counter),
        .encrypt(encrypt),
        .read_key_in(read_key_in),
        .load_round_key(load_round_key),
        .save_round_key(save_round_key),
        .addr_round_key_mem(addr_round_key_mem),
        //outputs
        //to core
        .round_key_delayed(round_key_delayed),
        .round_key_last(round_key_last)
    );
endmodule