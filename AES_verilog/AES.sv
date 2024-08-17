module AES (
    input wire clk,
    input wire rst,
    input wire [7:0] data_in,
    input wire [7:0] key_in,
    input wire start,
    input wire in_encrypt,
    input wire idle,

    output reg output_valid,
    output wire [3:0] out_byte_num,
    output reg [7:0] data_out
);
    wire encrypt;
    wire first_round;
    wire [3:0] round_counter;
    wire read_key_in;
    wire load_round_key;
    wire save_round_key;
    wire [3:0] inner_state_counter;
    wire rst_synch;
    wire [7:0] addr_round_key_mem;
    AES_DataPath aes_dp (
        .clk(clk),
        .rst(rst),
        .rst_synch(rst_synch),
        //from user
        .data_in(data_in),
        .key_in(key_in),
        //from controller
        .addr_round_key_mem(addr_round_key_mem),
        .en_generator(en_generator),
        .encrypt(encrypt),
        .first_round(first_round),
        .round_counter(round_counter),
        .read_key_in(read_key_in),
        .load_round_key(load_round_key),
        .save_round_key(save_round_key),
        //to controller
        .inner_state_counter(inner_state_counter),
        //to user
        .data_out(data_out)
    );
    AES_Controller aes_c (
        .clk(clk),
        .rst(rst),
        //from user
        .start(start),
        .in_encrypt(in_encrypt),
        .idle(idle),
        //to user
        .out_byte_num(out_byte_num),
        .output_valid(output_valid),
        //from datapath
        .inner_state_counter(inner_state_counter),
        //to datapath
        .rst_synch(rst_synch),
        .en_generator(en_generator),
        .addr_round_key_mem(addr_round_key_mem),
        .encrypt(encrypt),
        .first_round(first_round),
        .round_counter(round_counter),
        .read_key_in(read_key_in),
        .load_round_key(load_round_key),
        .save_round_key(save_round_key)
    );
endmodule