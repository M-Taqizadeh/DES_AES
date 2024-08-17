module AES_DataPath_Key_Schedule_Generator (
    input wire clk,
    input wire rst,
    input wire [7:0] key_in,
    //from controller
    input wire en_generator,
    input wire [3:0] round_counter,
    input wire encrypt,
    input wire en_rcon,
    input wire read_key_in,
    input wire add_new_word_to_r4,
    input wire add_modified_last_word_to_r0,
    input wire en_rot_word,
    //outputs
    //to core
    output reg [7:0] round_key_delayed,
    output reg [7:0] round_key_last,
    //to key schedule mem
    output reg [7:0] round_key_fast
);
    reg [3:0] round_counter_1;
    reg [3:0] round_counter_2;
    reg [3:0] round_counter_3;
    reg [3:0] round_counter_4;
    always@(posedge clk)begin
        round_counter_1 <= round_counter;
        round_counter_2 <= round_counter_1;
        round_counter_3 <= round_counter_2;
        round_counter_4 <= round_counter_3;
    end
    assign round_key_fast = read_key_in ? key_in : round_key_last;
    reg [7:0] sr15;
    reg [7:0] sr14;
    reg [7:0] sr13;
    reg [7:0] sr12;
    reg [7:0] sr11;
    reg [7:0] sr10;
    reg [7:0] sr9;
    reg [7:0] sr8;
    reg [7:0] sr7;
    reg [7:0] sr6;
    reg [7:0] sr5;
    reg [7:0] sr4;
    reg [7:0] sr3;
    reg [7:0] sr2;
    reg [7:0] sr1;
    reg [7:0] sr0;
    always@(posedge clk)begin
        if(en_generator)begin
            sr15 <= read_key_in ? key_in : round_key_last;
            sr14 <= sr15;
            sr13 <= sr14;
            sr12 <= sr13;
            sr11 <= sr12;
            sr10 <= sr11;
            sr9 <= sr10;
            sr8 <= sr9;
            sr7 <= sr8;
            sr6 <= sr7;
            sr5 <= sr6;
            sr4 <= sr5;
            sr3 <= add_new_word_to_r4 ? sr4 ^ round_key_last : sr4;
            sr2 <= sr3;
            sr1 <= sr2;
            sr0 <= sr1;
        end
    end

    wire [7:0] sbox_out;
    bSbox bsbox(
        .A(en_rot_word ? sr9 : sr13),
        .encrypt(encrypt),
        .Q(sbox_out)
    );
    wire [7:0] round_const;
    rcon round_cons_mem(
        .clk(clk),
        .addr(round_counter_4),
        .out(round_const)
    );
    wire [7:0] effective_round_const;
    assign effective_round_const = round_const & {8{en_rcon}};
    assign round_key_delayed = sr12;
    assign round_key_last = add_modified_last_word_to_r0 ? 
                            effective_round_const ^ sbox_out ^ sr0 : sr0;
endmodule