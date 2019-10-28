# Calculates Modular Exponentiation of a large integer

# Get input from user
puts "Enter an x value:"
s = Integer(gets.chomp)
puts "Enter a y value:"
r = Integer(gets.chomp)
puts "Enter a mod value:"
n = Integer(gets.chomp)
p = 1

# Calculate
while r > 0
    if r % 2 == 1
        p = p * s % n
    end
    s = s * s % n
    r = Integer(r / 2)
    #puts(r)
end

# Return the value
puts "Result: ", p