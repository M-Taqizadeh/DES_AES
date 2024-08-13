module Mix_Column (
    input wire rst,
    input wire clk,
    input wire en,
    input wire [7:0] d_in,
    output reg [7:0] d_out0,
    output reg [7:0] d_out1,
    output reg [7:0] d_out2,
    output reg [7:0] d_out3,
);
    wire [7:0] d_in_tiems2, d_in_tiems3;
    wire [7:0] r0_in, r1_in, r2_in, r3_in;
    assign d_in_tiems2 = d_in[7] ? d_in << 1 : (d_in << 1) ^ 8'h1b;
    assign d_in_tiems3 = d_in_tiems2 ^ d_in;
    assign r0_in = d_in ^ (en & d_out1)
    assign r1_in = d_in ^ (en & d_out2)
    assign r2_in = d_in_tiems3 ^ (en & d_out3)
    assign r3_in = d_in_tiems2 ^ (en & d_out0)
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