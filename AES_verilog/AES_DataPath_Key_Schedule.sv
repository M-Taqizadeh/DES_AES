module AES_DataPath_Key_Schedule (
    input wire clk,
    input wire rst,
    input wire [7:0]key_in,
    //from inner state counter
    input wire [3:0] inner_state_counter,
    //from controller
    input wire en_generator,
    input wire [3:0] round_counter,
    input wire encrypt,
    input wire read_key_in,
    input wire load_round_key,
    input wire save_round_key,
    input wire [7:0] addr_round_key_mem,
    //outputs
    //to core
    output reg [7:0] round_key_delayed,
    output reg [7:0] round_key_last
);
    wire en_rcon;
    wire add_new_word_to_r4;
    wire add_modified_last_word_to_r0;
    wire en_rot_word;
    AES_DataPath_Key_Schedule_Generator_Controller aes_dp_ks_g_c(
        .inner_state_counter(inner_state_counter),
        .en_rcon(en_rcon),
        .add_new_word_to_r4(add_new_word_to_r4),
        .add_modified_last_word_to_r0(add_modified_last_word_to_r0),
        .en_rot_word(en_rot_word)
    );
    reg [7:0] round_key_fast;
    wire [7:0] generated_round_key_delayed;
    wire [7:0] generated_round_key_last;
    wire [7:0] loaded_round_key_delayed;
    wire [7:0] loaded_round_key_last;
    assign round_key_delayed = load_round_key ? loaded_round_key_delayed : generated_round_key_delayed;
    assign round_key_last = load_round_key ? loaded_round_key_last : generated_round_key_last;
    
    AES_DataPath_Key_Schedule_Generator aes_dp_ks_g(
        .clk(clk),
        .rst(rst),
        .key_in(key_in),
        //from controller
        .en_generator(en_generator),
        .round_counter(round_counter),
        .en_rcon(en_rcon),
        .encrypt(encrypt),
        .read_key_in(read_key_in),
        .add_new_word_to_r4(add_new_word_to_r4),
        .add_modified_last_word_to_r0(add_modified_last_word_to_r0),
        .en_rot_word(en_rot_word),
        //outputs
        //to core
        .round_key_delayed(generated_round_key_delayed),
        .round_key_last(generated_round_key_last),
        //to key schedule mem
        .round_key_fast(round_key_fast)
    );
    AES_DataPath_Key_Schedule_mem aes_dp_ks_mem(
        .clk(clk),
        .in_round_key(round_key_fast),
        .addr(addr_round_key_mem),
        .write_en(save_round_key),
        .out_round_key(loaded_round_key_last),
        .out_round_key_delayed(loaded_round_key_delayed)
    );
endmodule
