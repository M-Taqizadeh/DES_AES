module Byte_Permutation_Unit_DataPath (
    input wire clk,
    input wire rst,
    input wire [7:0] in_byte,
    input wire c0, c1, c2,
    input wire [1:0] c3,
    output reg [7:0] out_byte
);
    wire [7:0] in_sr_0;
    wire [7:0] in_sr_1;
    wire [7:0] in_sr_2;
    wire [7:0] out_sr_0;
    wire [7:0] out_sr_1;
    wire [7:0] out_sr_2;
    Shift_Reg_4 sr0 (
        .clk(clk),
        .rst(rst),
        .in_byte(in_sr_0),
        .out_byte(out_sr_0));
    Shift_Reg_4 sr1 (
        .clk(clk),
        .rst(rst),
        .in_byte(in_sr_1),
        .out_byte(out_sr_1));
    Shift_Reg_4 sr2 (
        .clk(clk),
        .rst(rst),
        .in_byte(in_sr_2),
        .out_byte(out_sr_2));
    assign in_sr_0 = c0 ? out_sr_2 : in_byte;
    assign in_sr_1 = c1 ? out_sr_2 : out_sr_0;
    assign in_sr_2 = c2 ? out_sr_2 : out_sr_1;
    always @(*) begin
        case (c3)
            2'b00 : out_byte = in_byte;
            2'b01 : out_byte = out_sr_0;
            2'b10 : out_byte = out_sr_1;
            2'b11 : out_byte = out_sr_2;
            default: out_byte = 4'b0000;
        endcase
    end
    
endmodule