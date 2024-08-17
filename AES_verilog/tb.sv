`define HALF_CLK 5
`define CLK (2*`HALF_CLK)
module tb();
    reg clk;
    always @(clk)begin
        #`HALF_CLK
        clk <= ~clk;
    end
    initial begin
        clk <= 1'b1;
    end
    reg rst;
    reg [7:0] data_in;
    reg [7:0] key_in;
    reg start;
    reg in_encrypt;
    reg idle;
    reg output_valid;
    reg [3:0] out_byte_num;
    reg [7:0] data_out;
    AES aes (
        .clk(clk),
        .rst(rst),
        .data_in(data_in),
        .key_in(key_in),
        .start(start),
        .in_encrypt(in_encrypt),
        .idle(idle),
        .output_valid(output_valid),
        .out_byte_num(out_byte_num),
        .data_out(data_out)
    );
    reg [127:0] key_mem [0:7];
    reg [127:0] calculated_plaintext_mem [0:7];
    reg [127:0] calculated_ciphertext_mem [0:7];
    reg [127:0] expected_plaintext_mem [0:7];
    reg [127:0] expected_ciphertext_mem [0:7];

    reg [2:0] test_addr;
    wire [127:0] expected_plaintext;
    wire [127:0] expected_ciphertext;
    wire [127:0] key;
    assign expected_plaintext = expected_plaintext_mem[test_addr];
    assign expected_ciphertext = expected_ciphertext_mem[test_addr];
    assign key = key_mem[test_addr];
     
    wire [7:0] key_byte;
    wire [7:0] plaintext_byte;
    wire [7:0] ciphertext_byte;
    assign key_byte = key[127 - (8*out_byte_num) -: 8];
    assign plaintext_byte = expected_plaintext[127 - (8*out_byte_num) -: 8];
    assign ciphertext_byte = expected_ciphertext[127 - (8*out_byte_num) -: 8];
    assign data_in = in_encrypt ? plaintext_byte : ciphertext_byte;
    assign key_in = key_byte;

    reg [127:0] calculated_output;
    reg output_valid_delayed;
    reg [2:0] test_addr_delayed_1;
    reg [2:0] test_addr_delayed_2;
    reg in_encrypt_delayed_1;
    reg in_encrypt_delayed_2;
    always @(posedge clk)begin
        output_valid_delayed <= output_valid;
        test_addr_delayed_1 <= test_addr;
        test_addr_delayed_2 <= test_addr_delayed_1;
        in_encrypt_delayed_1 <= in_encrypt;
        in_encrypt_delayed_2 <= in_encrypt_delayed_1;
        if(output_valid)begin
            calculated_output[127 - (8*out_byte_num) -: 8] <= data_out;
        end
        if(~output_valid && output_valid_delayed)begin
            if(in_encrypt_delayed_2)begin
                calculated_ciphertext_mem[test_addr_delayed_2] <= calculated_output;
            end else begin
                calculated_plaintext_mem[test_addr_delayed_2] <= calculated_output;
            end
        end
    end
    initial begin
        $readmemh("tb_key_mem.txt", key_mem);
        $readmemh("tb_plaintext_mem.txt", expected_plaintext_mem);
        $readmemh("tb_ciphertext_mem.txt", expected_ciphertext_mem);
        start <= 1'b0;
        in_encrypt <= 1'b1;
        idle <= 1'b0;
        rst <= 1'b0;
        #`CLK
        rst <= 1'b1;
        #`CLK
        rst <= 1'b0;
        
        in_encrypt <= 1'b0;
        test_addr <= 3'b000;
        
        start <= 1'b1;
        #`CLK
        start <= 1'b0;
        for (int i = 0; i < 8; i += 1)begin
            #((22 * 16) * `CLK)
            test_addr <= test_addr + 1;
        end
        
        idle <= 1'b1;
        in_encrypt <= 1'b1;
        test_addr <= 3'b000;
        #`CLK
        idle <= 1'b0;
        
        start <= 1'b1;
        #`CLK
        start <= 1'b0;
        for (int i = 0; i < 8; i += 1)begin

            #((11 * 16) * `CLK)
            test_addr <= test_addr + 1;
        end
        #(2*`CLK)
        $stop;
    end
endmodule