module AES_DataPath_Key_Schedule_mem (
    input wire clk,
    input wire [7:0] in_round_key,
    input wire [7:0] addr,
    input wire write_en,
    output reg [7:0] out_round_key,
    output reg [7:0] out_round_key_delayed
);
    reg [7:0] mem [0:175]; // 175 = 11(num_rounds) * 16(subkeys_per_round) - 1
    always @(posedge clk)begin
        if(write_en)begin
            mem[addr] <= in_round_key;
        end
    end
    reg [7:0] out_round_key_1;
    reg [7:0] out_round_key_2;
    reg [7:0] out_round_key_3;
    reg [7:0] out_round_key_4;
    always@(posedge clk)begin
        out_round_key_1 <= out_round_key;
        out_round_key_2 <= out_round_key_1;
        out_round_key_3 <= out_round_key_2;
        out_round_key_4 <= out_round_key_3;
    end
    
    assign out_round_key = mem[addr];
    assign out_round_key_delayed = out_round_key_4;
endmodule