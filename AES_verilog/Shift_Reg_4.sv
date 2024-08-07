module Shift_Reg_4 (
    input wire clk,
    input wire rst,
    input wire [7:0] in_byte,
    output reg [7:0] out_byte
);
    reg [7:0] r [0:3];
    assign out_byte = r[3];
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            r[0] <= 8'b0;
            r[1] <= 8'b0;
            r[2] <= 8'b0;
            r[3] <= 8'b0;
        end else begin
            r[0] <= in_byte;
            r[1] <= r[0];
            r[2] <= r[1];
            r[3] <= r[2];
        end
    end
endmodule