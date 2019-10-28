puts "Enter an x value:"
s = Integer(gets.chomp)
puts "Enter a y value:"
r = Integer(gets.chomp)
puts "Enter a mod value:"
n = Integer(gets.chomp)
p = 1

while r > 0
    if r % 2 == 1
        p = p * s % n
    end
    s = s * s % n
    r = Integer(r / 2)
    #puts(r)
end

puts "Result: ", p