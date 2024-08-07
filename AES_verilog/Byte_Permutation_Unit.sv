module Byte_Permutation_Unit(
    input wire clk,
    input wire rst,
    input wire rst_synch,
    input wire shift_left,
    input wire [7:0] in_byte,
    output reg [7:0] out_byte
);
    wire c0, c1, c2;
    wire [1:0] c3;
    Byte_Permutation_Unit_Controller BPUC (
        .clk(clk),
        .rst(rst),
        .rst_synch(rst_synch),
        .shift_left(shift_left),
        .c0(c0),
        .c1(c1),
        .c2(c2),
        .c3(c3)  
    );
    Byte_Permutation_Unit_DataPath BPUDP (
        .clk(clk),
        .rst(rst),
        .in_byte(in_byte),
        .c0(c0),
        .c1(c1),
        .c2(c2),
        .c3(c3),
        .out_byte(out_byte)
    );
endmodule