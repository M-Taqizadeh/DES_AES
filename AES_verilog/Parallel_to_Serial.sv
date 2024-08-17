module Parallel_to_Serial (
    input wire clk,
    input wire rst,
    input wire en_paralle,
    input wire [7:0] serial_d_in,
    input wire [7:0] parallel_d_in0,
    input wire [7:0] parallel_d_in1,
    input wire [7:0] parallel_d_in2,
    input wire [7:0] parallel_d_in3,
    output reg [7:0] d_out
);
    wire [7:0] r1_in, r2_in, r3_in, r_serial_in;
    reg [7:0] r1, r2, r3, r_serial;
    assign d_out = en_paralle ? parallel_d_in0 : r1;
    assign r1_in = en_paralle ? parallel_d_in1 : r2;
    assign r2_in = en_paralle ? parallel_d_in2 : r3;
    assign r3_in = en_paralle ? parallel_d_in3 : r_serial;
    assign r_serial_in = serial_d_in;
    always @(posedge clk or posedge rst)begin
        if(rst)begin
            r1 <= 8'b0; 
            r2 <= 8'b0;
            r3 <= 8'b0;
            r_serial <= 8'b0;
        end else begin
            r1 <= r1_in; 
            r2 <= r2_in;
            r3 <= r3_in;
            r_serial <= r_serial_in;
        end
    end
endmodule