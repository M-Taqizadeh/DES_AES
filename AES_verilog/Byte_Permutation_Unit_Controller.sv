// requires 12 clocks for initial loading but can wrok with no dead cycles afterwards
module Byte_Permutation_Unit_Controller (
    input wire clk,
    input wire rst,
    input wire rst_synch,
    input wire shift_left,
    output reg c0,
    output reg c1,
    output reg c2,
    output reg [1:0] c3  
);
    reg [4:0] counter;
    always @(posedge clk or posedge rst) begin
        if(rst)begin
            counter <= 5'b0;
        end else begin
            if (rst_synch)begin
                counter <= 5'b0;
            end else if(counter == 5'b11011)begin
                counter <= 5'b01100;
            end else begin
                counter <= counter + 1;
            end
        end
    end
    always @(*)begin
        case (counter)
            5'b00000 : {c0, c1, c2, c3} = 5'b00011;
            5'b00001 : {c0, c1, c2, c3} = 5'b00011;
            5'b00010 : {c0, c1, c2, c3} = 5'b00011;
            5'b00011 : {c0, c1, c2, c3} = 5'b00011;
            5'b00100 : {c0, c1, c2, c3} = 5'b00011;
            5'b00101 : {c0, c1, c2, c3} = 5'b00011;
            5'b00110 : {c0, c1, c2, c3} = 5'b00011;
            5'b00111 : {c0, c1, c2, c3} = 5'b00011;
            5'b01000 : {c0, c1, c2, c3} = 5'b00011;
            5'b01001 : {c0, c1, c2, c3} = 5'b00011;
            5'b01010 : {c0, c1, c2, c3} = 5'b00011;
            5'b01011 : {c0, c1, c2, c3} = 5'b00011;
            5'b01100 : {c0, c1, c2, c3} = 5'b00011;
            5'b01101 : {c0, c1, c2, c3} = shift_left ? 5'b00110 : 5'b10000;
            5'b01110 : {c0, c1, c2, c3} = 5'b01001;
            5'b01111 : {c0, c1, c2, c3} = shift_left ? 5'b10000 : 5'b00110;
            5'b10000 : {c0, c1, c2, c3} = 5'b00011;
            5'b10001 : {c0, c1, c2, c3} = shift_left ? 5'b00110 : 5'b01001;
            5'b10010 : {c0, c1, c2, c3} = 5'b01001;
            5'b10011 : {c0, c1, c2, c3} = shift_left ? 5'b01001 : 5'b00110;
            5'b10100 : {c0, c1, c2, c3} = 5'b00011;
            5'b10101 : {c0, c1, c2, c3} = 5'b00110;
            5'b10110 : {c0, c1, c2, c3} = 5'b00011;
            5'b10111 : {c0, c1, c2, c3} = 5'b00110;
            5'b11000 : {c0, c1, c2, c3} = 5'b00011;
            5'b11001 : {c0, c1, c2, c3} = 5'b00011;
            5'b11010 : {c0, c1, c2, c3} = 5'b00011;
            5'b11011 : {c0, c1, c2, c3} = shift_left ? 5'b00000 : 5'b00010;
            default  : {c0, c1, c2, c3} = 5'b00000;
        endcase
    end
endmodule