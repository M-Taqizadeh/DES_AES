`define HALF_CLK 5
`define CLK (2*`HALF_CLK)
module tb_Byte_Permutation_Unit();
    reg clk, rst, c0, c1, c2;
    reg [7:0] in_byte, out_byte;
    // reg [1:0] c3;
    Byte_Permutation_Unit BPU (
        .clk(clk),
        .rst(rst),
        .rst_synch(1'b0),
        .shift_left(1'b0),
        .in_byte(in_byte),
        // .c0(c0),
        // .c1(c1),
        // .c2(c2),
        // .c3(c3),
        .out_byte(out_byte)
    );
    always @(clk)begin
        #`HALF_CLK
        clk <= ~clk;
    end
    reg [3:0] addr;
    assign in_byte = {4'b0, addr};
    always @(posedge clk or posedge rst) begin
        if(rst)begin
            addr <= 4'b0;
        end else begin
            addr <= addr + 1;
        end
    end

    // assign c0 = 1'b0;
    // assign c1 = 1'b0;
    // assign c2 = 1'b0;
    // assign c3 = 2'b11;
    
    initial begin
        rst <= 1'b0;
        clk <= 1'b1;
        # `CLK
        rst <= 1'b1;
        # `CLK
        rst <= 1'b0;
        # (200 * `CLK)
        $stop;
    end
endmodule