module AES_DataPath_Key_Schedule_Generator_Controller (
    input wire [3:0] inner_state_counter,
    output reg en_rcon,
    output reg add_new_word_to_r4,
    output reg add_modified_last_word_to_r0,
    output reg en_rot_word
);
    always @(*)begin
        case (inner_state_counter)
            4'b0000 : add_new_word_to_r4 = 1'b1;
            4'b0001 : add_new_word_to_r4 = 1'b1;
            4'b0010 : add_new_word_to_r4 = 1'b1;
            4'b0011 : add_new_word_to_r4 = 1'b1;
            4'b0100 : add_new_word_to_r4 = 1'b1;
            4'b0101 : add_new_word_to_r4 = 1'b1;
            4'b0110 : add_new_word_to_r4 = 1'b1;
            4'b0111 : add_new_word_to_r4 = 1'b1;
            4'b1000 : add_new_word_to_r4 = 1'b1;
            4'b1001 : add_new_word_to_r4 = 1'b1;
            4'b1010 : add_new_word_to_r4 = 1'b1;
            4'b1011 : add_new_word_to_r4 = 1'b1;
            4'b1100 : add_new_word_to_r4 = 1'b0; 
            4'b1101 : add_new_word_to_r4 = 1'b0;
            4'b1110 : add_new_word_to_r4 = 1'b0;
            4'b1111 : add_new_word_to_r4 = 1'b0;
            default : add_new_word_to_r4 = 1'b0;
        endcase
    end
    always @(*)begin
        case (inner_state_counter)
            4'b0000 : add_modified_last_word_to_r0 = 1'b1;
            4'b0001 : add_modified_last_word_to_r0 = 1'b1;
            4'b0010 : add_modified_last_word_to_r0 = 1'b1;
            4'b0011 : add_modified_last_word_to_r0 = 1'b1;
            4'b0100 : add_modified_last_word_to_r0 = 1'b0;
            4'b0101 : add_modified_last_word_to_r0 = 1'b0;
            4'b0110 : add_modified_last_word_to_r0 = 1'b0;
            4'b0111 : add_modified_last_word_to_r0 = 1'b0;
            4'b1000 : add_modified_last_word_to_r0 = 1'b0;
            4'b1001 : add_modified_last_word_to_r0 = 1'b0;
            4'b1010 : add_modified_last_word_to_r0 = 1'b0;
            4'b1011 : add_modified_last_word_to_r0 = 1'b0;
            4'b1100 : add_modified_last_word_to_r0 = 1'b0;
            4'b1101 : add_modified_last_word_to_r0 = 1'b0;
            4'b1110 : add_modified_last_word_to_r0 = 1'b0;
            4'b1111 : add_modified_last_word_to_r0 = 1'b0;
            default : add_modified_last_word_to_r0 = 1'b0;
        endcase
    end
    always @(*)begin
        case (inner_state_counter)
            4'b0000 : en_rot_word = 1'b0;
            4'b0001 : en_rot_word = 1'b0;
            4'b0010 : en_rot_word = 1'b0;
            4'b0011 : en_rot_word = 1'b1;
            4'b0100 : en_rot_word = 1'b0;
            4'b0101 : en_rot_word = 1'b0;
            4'b0110 : en_rot_word = 1'b0;
            4'b0111 : en_rot_word = 1'b0;
            4'b1000 : en_rot_word = 1'b0;
            4'b1001 : en_rot_word = 1'b0;
            4'b1010 : en_rot_word = 1'b0;
            4'b1011 : en_rot_word = 1'b0;
            4'b1100 : en_rot_word = 1'b0;
            4'b1101 : en_rot_word = 1'b0;
            4'b1110 : en_rot_word = 1'b0;
            4'b1111 : en_rot_word = 1'b0;
            default : en_rot_word = 1'b0;
        endcase
    end
    always @(*)begin
        case (inner_state_counter)
            4'b0000 : en_rcon = 1'b1;
            4'b0001 : en_rcon = 1'b0;
            4'b0010 : en_rcon = 1'b0;
            4'b0011 : en_rcon = 1'b0;
            4'b0100 : en_rcon = 1'b0;
            4'b0101 : en_rcon = 1'b0;
            4'b0110 : en_rcon = 1'b0;
            4'b0111 : en_rcon = 1'b0;
            4'b1000 : en_rcon = 1'b0;
            4'b1001 : en_rcon = 1'b0;
            4'b1010 : en_rcon = 1'b0;
            4'b1011 : en_rcon = 1'b0;
            4'b1100 : en_rcon = 1'b0;
            4'b1101 : en_rcon = 1'b0;
            4'b1110 : en_rcon = 1'b0;
            4'b1111 : en_rcon = 1'b0;
            default : en_rcon = 1'b0;
        endcase
    end
endmodule