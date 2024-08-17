`define HALF_CLK 5
`define CLK (2*`HALF_CLK)
module tb_sbox();
    reg clk;
    reg rst;
    reg [7:0] expected_sbox [0:255];
    reg [7:0] expected_inv_sbox [0:255];
    reg [7:0] calculated_sbox [0:255];
    reg [7:0] calculated_inv_sbox [0:255];
    reg [7:0] addr;
    wire [7:0] s_box_out;
    wire [7:0] inv_s_box_out;
    
    bSbox s_box(addr, 1'b1, s_box_out);
    bSbox inv_s_box(addr, 1'b0, inv_s_box_out);
    
    always @(clk)begin
        #`HALF_CLK
        clk <= ~clk;
    end
    always @(posedge clk or posedge rst)begin
        if(rst)begin
            addr <= 8'b0;
        end else begin
            calculated_sbox[addr]<= s_box_out;
            calculated_inv_sbox[addr]<= inv_s_box_out;
            if (s_box_out != expected_sbox[addr])begin
                $display("sbox %d has an error", addr);
            end
            if (inv_s_box_out != expected_inv_sbox[addr])begin
                $display("inv_sbox %d has an error", addr);
            end
            addr <= addr + 1;
        end
    end
    initial begin
        $readmemh("S_Box_data_hex.txt", expected_sbox);
        $readmemh("Inv_S_Box_data_hex.txt", expected_inv_sbox);
        rst <= 1'b1;
        #`CLK
        rst <= 1'b0;
        clk <= 1'b0;
        #(300 * `CLK)
        $stop;
    end
endmodule