my_sum = 0

function generate_combinations(nums)
    function combine(index, current_result)
        if index == length(nums)+1
            return [current_result]
        end
        results = []
        current_num = nums[index]

        #Addition
        append!(results,combine(index+1, current_result + current_num))

        #Multiplication
        append!(results,combine(index+1, current_result * current_num))

        #concatenation - part 2 only
        append!(results,combine(index+1, parse(Int64,string(current_result) * string(current_num))))
        
        return results
    end

    return combine(2, nums[1])
end

nums = [15, 6]
all_results = generate_combinations(nums)

println(all_results)
#println(issubset(3267, all_results))

function is_possible(res, vals)
    res = parse(Int64, res)
    nums = [parse(Int64,x) for x in split(vals, " ")]
    
    all_combs = generate_combinations(nums)

    if res in all_combs
        return res
    else 
        return 0
    end
end

open("input.txt") do f

    line = 0

    while ! eof(f)
        s = readline(f)
        #print(s)
        res, vals = split(s, ": ")
        #print(res,  vals)
        global my_sum += is_possible(res,vals)
    end
end

println("Result: $my_sum")
