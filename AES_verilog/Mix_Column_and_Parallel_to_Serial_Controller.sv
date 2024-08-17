module Mix_Column_and_Parallel_to_Serial_Controller (
    input wire [3:0] inner_state_counter,
    output reg en_parallel_load
);
    always @(*)begin
        case (inner_state_counter)
            4'b0000 : en_parallel_load = 1'b1;
            4'b0001 : en_parallel_load = 1'b0;
            4'b0010 : en_parallel_load = 1'b0;
            4'b0011 : en_parallel_load = 1'b0;
            4'b0100 : en_parallel_load = 1'b1;
            4'b0101 : en_parallel_load = 1'b0;
            4'b0110 : en_parallel_load = 1'b0;
            4'b0111 : en_parallel_load = 1'b0;
            4'b1000 : en_parallel_load = 1'b1;
            4'b1001 : en_parallel_load = 1'b0;
            4'b1010 : en_parallel_load = 1'b0;
            4'b1011 : en_parallel_load = 1'b0;
            4'b1100 : en_parallel_load = 1'b1;
            4'b1101 : en_parallel_load = 1'b0;
            4'b1110 : en_parallel_load = 1'b0;
            4'b1111 : en_parallel_load = 1'b0;
            default : en_parallel_load = 1'b0;
        endcase
    end
endmodule