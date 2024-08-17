module Byte_Permutation_Unit_Controller (
    input wire shift_left,
    input wire [3:0] inner_state_counter,
    output reg c0,
    output reg c1,
    output reg c2,
    output reg [1:0] c3  
);
    always @(*)begin
        case (inner_state_counter)
            4'b0000 : {c0, c1, c2, c3} = 5'b00011;
            4'b0001 : {c0, c1, c2, c3} = shift_left ? 5'b00110 : 5'b10000;
            4'b0010 : {c0, c1, c2, c3} = 5'b01001;
            4'b0011 : {c0, c1, c2, c3} = shift_left ? 5'b10000 : 5'b00110;
            4'b0100 : {c0, c1, c2, c3} = 5'b00011;
            4'b0101 : {c0, c1, c2, c3} = shift_left ? 5'b00110 : 5'b01001;
            4'b0110 : {c0, c1, c2, c3} = 5'b01001;
            4'b0111 : {c0, c1, c2, c3} = shift_left ? 5'b01001 : 5'b00110;
            4'b1000 : {c0, c1, c2, c3} = 5'b00011;
            4'b1001 : {c0, c1, c2, c3} = 5'b00110;
            4'b1010 : {c0, c1, c2, c3} = 5'b00011;
            4'b1011 : {c0, c1, c2, c3} = 5'b00110;
            4'b1100 : {c0, c1, c2, c3} = 5'b00011;
            4'b1101 : {c0, c1, c2, c3} = 5'b00011;
            4'b1110 : {c0, c1, c2, c3} = 5'b00011;
            4'b1111 : {c0, c1, c2, c3} = 5'b00011;
            
            default  : {c0, c1, c2, c3} = 5'b00000;
        endcase
    end
endmodule