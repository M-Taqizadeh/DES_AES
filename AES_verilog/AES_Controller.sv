`define IDLE                 2'b00
`define ENCRYPT              2'b01
`define DECRYPT_KEY_PROCESS  2'b10
`define DECRYPT_DATA_PROCESS 2'b11
module AES_Controller (
    input wire clk,
    input wire rst,
    //from user
    input wire start,
    input wire in_encrypt,
    input wire idle,
    //to user
    output wire [3:0] out_byte_num,
    output reg output_valid,
    //from datapath
    input wire [3:0] inner_state_counter,
    //to datapath
    output reg rst_synch,
    output reg en_generator,
    output reg [7:0] addr_round_key_mem,
    output reg encrypt,
    output reg first_round,
    output reg [3:0] round_counter,
    output reg read_key_in,
    output reg load_round_key,
    output reg save_round_key
    );
    reg [1:0] current_macro_state;
    reg [1:0] next_macro_state;
    reg [3:0] round_cap;
    always@(*)begin
        case (current_macro_state)
            `IDLE    : begin
                {rst_synch, encrypt, en_generator, load_round_key, save_round_key} = 5'b10000;
                round_cap = 4'b0;
                addr_round_key_mem = 8'b0;
                output_valid = 1'b0;
            end
            `ENCRYPT : begin
                {rst_synch, encrypt, en_generator, load_round_key, save_round_key} = 5'b01100;
                // round_cap = 4'b1001;
                round_cap = 4'b1010;
                addr_round_key_mem = 8'b0;
                output_valid = round_counter == round_cap;
            end
            `DECRYPT_KEY_PROCESS :begin
                {rst_synch, encrypt, en_generator, load_round_key, save_round_key} = 5'b01101;
                round_cap = 4'b1010;
                addr_round_key_mem = {round_counter, inner_state_counter};
                output_valid = 1'b0;
            end
            `DECRYPT_DATA_PROCESS :begin
                {rst_synch, encrypt, en_generator, load_round_key, save_round_key} = 5'b00010;
                round_cap = 4'b1010;
                addr_round_key_mem = {4'b1010 - round_counter, inner_state_counter};
                output_valid = round_counter == round_cap;
            end
            default  : begin
                {rst_synch, encrypt, en_generator, load_round_key, save_round_key} = 5'b10000;
                round_cap = 4'b0;
                addr_round_key_mem = 4'b0;
                output_valid = 1'b0;
            end
        endcase
    end
    always@(*)begin
        case (current_macro_state)
            `IDLE                 : next_macro_state = start ? (in_encrypt ? `ENCRYPT : `DECRYPT_KEY_PROCESS) : `IDLE;
            `ENCRYPT              : next_macro_state = idle ? `IDLE : `ENCRYPT;
            `DECRYPT_KEY_PROCESS  : next_macro_state = idle ? `IDLE :
                                                       (round_counter == round_cap && inner_state_counter == 4'b1111) ?
                                                       `DECRYPT_DATA_PROCESS : `DECRYPT_KEY_PROCESS;
            `DECRYPT_DATA_PROCESS : next_macro_state = idle ? `IDLE :
                                                       (round_counter == round_cap && inner_state_counter == 4'b1111) ?
                                                       `DECRYPT_KEY_PROCESS : `DECRYPT_DATA_PROCESS;
            default               : next_macro_state = `IDLE;
        endcase
    end
    always @(posedge clk or posedge rst)begin
        if(rst)begin
            current_macro_state <= `IDLE;
        end else begin
            current_macro_state <= next_macro_state;
        end
    end

    wire en_round_counter;
    always @(posedge clk or posedge rst)begin
        if(rst)begin
            round_counter <= 4'b0;
        end else if(rst_synch)begin
            round_counter <= 4'b0;
        end else if(en_round_counter)begin
            if(round_counter == round_cap)begin
                round_counter <= 4'b0;
            end else begin
                round_counter <= round_counter + 1;
            end
        end
    end
    assign en_round_counter = (inner_state_counter == 4'b1111);
    assign out_byte_num = inner_state_counter;
    assign first_round = round_counter == 4'b0000;
    assign read_key_in = first_round;
endmodule