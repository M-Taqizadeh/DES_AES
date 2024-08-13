module Mix_Column (
    input wire rst,
    input wire clk,
    input wire en,
    input wire encrypt,
    input wire [7:0] d_in,
    output reg [7:0] d_out0,
    output reg [7:0] d_out1,
    output reg [7:0] d_out2,
    output reg [7:0] d_out3,
);
    wire [7:0] d_in_times2
    wire [7:0] d_in_times3;
    wire [7:0] d_in_times4;
    wire [7:0] d_in_times5;
    wire [7:0] d_in_times6;
    wire [7:0] d_in_times7;
    wire [7:0] d_in_times8;
    wire [7:0] d_in_times9;
    wire [7:0] d_in_times10;
    wire [7:0] d_in_times11;
    wire [7:0] d_in_times12;
    wire [7:0] d_in_times13;
    wire [7:0] d_in_times14;
    wire [7:0] r0_in, r1_in, r2_in, r3_in;
    
    assign d_in_times2 = d_in[7] ? d_in << 1 : (d_in << 1) ^ 8'h1b;
    assign d_in_times3 = d_in_times2 ^ d_in;
    assign d_in_times4 = d_in_times2[7] ? d_in_times2 << 1 : (d_in_times2 << 1) ^ 8'h1b;
    assign d_in_times5 = d_in_times4 ^ d_in;
    assign d_in_times6 = d_in_times3[7] ? d_in_times3 << 1 : (d_in_times3 << 1) ^ 8'h1b;
    assign d_in_times7 = d_in_times6 ^ d_in;
    assign d_in_times8 = d_in_times4[7] ? d_in_times4 << 1 : (d_in_times4 << 1) ^ 8'h1b;
    assign d_in_times9 = d_in_times_8 ^ d_in;
    assign d_in_times10 = d_in_times5[7] ? d_in_times5 << 1 : (d_in_times5 << 1) ^ 8'h1b;
    assign d_in_times11 = d_in_times_10 ^ d_in;
    assign d_in_times12 = d_in_times6[7] ? d_in_times6 << 1 : (d_in_times6 << 1) ^ 8'h1b;
    assign d_in_times13 = d_in_times_12 ^ d_in;
    assign d_in_times14 = d_in_times7[7] ? d_in_times7 << 1 : (d_in_times7 << 1) ^ 8'h1b;

    assign r0_in = (encrypt ? d_in : d_in_times9) ^ (en & d_out1)
    assign r1_in = (encrypt ? d_in : d_in_times13) ^ (en & d_out2)
    assign r2_in = (encrypt ? d_in_times3 : d_in_times11) ^ (en & d_out3)
    assign r3_in = (encrypt ? d_in_times2 : d_in_times14) ^ (en & d_out0)
    always @(posedge clk or posedge rst) begin
        if(rst)begin
            d_out0 <= 8'b0;
            d_out1 <= 8'b0;
            d_out2 <= 8'b0;
            d_out3 <= 8'b0;
        end else begin
            d_out0 <= r0_in;
            d_out1 <= r1_in;
            d_out2 <= r2_in;
            d_out3 <= r3_in;
        end
    end
endmodule