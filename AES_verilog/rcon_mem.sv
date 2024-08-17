module rcon (
    input wire clk,
    input wire [3:0] addr,
    output reg [7:0] out
);
    always @(posedge clk) begin
        case (addr)
            4'b0000 : out <= 8'h01;
            4'b0001 : out <= 8'h02;
            4'b0010 : out <= 8'h04;
            4'b0011 : out <= 8'h08;
            4'b0100 : out <= 8'h10;
            4'b0101 : out <= 8'h20;
            4'b0110 : out <= 8'h40;
            4'b0111 : out <= 8'h80;
            4'b1000 : out <= 8'h1b;
            4'b1001 : out <= 8'h36;
            4'b1010 : out <= 8'h6c;
            4'b1011 : out <= 8'hd8;
            4'b1100 : out <= 8'hab;
            4'b1101 : out <= 8'h4d;
            4'b1110 : out <= 8'h9a;
            4'b1111 : out <= 8'h2f;
            default : out <= 8'h00;
        endcase
    end
endmodule