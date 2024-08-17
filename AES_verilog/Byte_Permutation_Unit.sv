module Byte_Permutation_Unit(
    input wire clk,
    input wire rst,
    input wire rst_synch,
    input wire shift_left,
    input wire [3:0] inner_state_counter,
    input wire [7:0] in_byte,
    output reg [7:0] out_byte
);
    wire c0, c1, c2;
    wire [1:0] c3;
    Byte_Permutation_Unit_Controller BPUC (
        .shift_left(shift_left),
        .inner_state_counter(inner_state_counter),
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