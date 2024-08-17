module tb_AES_DataPath_Key_Schedule_Generator ();
    reg clk;
    reg rst;
    reg [7:0] key_in;
    reg [3:0] round_counter;
    reg en_rcon;
    reg read_key_in;
    reg add_new_word_to_r4;
    reg add_modified_last_word_to_r0;
    reg en_rot_word;
    reg round_key_delayed;
    reg round_key_last;
    AES_DataPath_Key_Schedule_Generator AES_DPKSG (
        .clk(clk),
        .rst(rst),
        .key_in(key_in),
        //from controller
        .round_counter(round_counter),
        .en_rcon(en_rcon),
        .read_key_in(read_key_in),
        .add_new_word_to_r4(add_new_word_to_r4),
        .add_modified_last_word_to_r0(add_modified_last_word_to_r0),
        .en_rot_word(en_rot_word),
        //outputs
        .round_key_delayed(round_key_delayed),
        .round_key_last(round_key_last)
    );
    
endmodule