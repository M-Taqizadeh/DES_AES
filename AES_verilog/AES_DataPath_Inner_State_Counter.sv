module AES_DataPath_Inner_State_Counter (
    input wire clk,
    input wire rst,
    input wire rst_synch,
    output reg [3:0] inner_state_counter
);
    always @(posedge clk or posedge rst) begin
        if(rst)begin
            inner_state_counter <= 4'b0;
        end else begin
            if (rst_synch)begin
                inner_state_counter <= 4'b0;
            end else begin
                inner_state_counter <= inner_state_counter + 1;
            end
        end
    end
endmodule