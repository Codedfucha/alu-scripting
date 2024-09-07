#!/usr/bin/env ruby
log_entry = ARGV[0]

sender = log_entry.match(/from:(.*?)\]/)[1]
receiver = log_entry.match(/to:(.*?)\]/)[1]
flags = log_entry.match(/flags:(.*?)\]/)[1]

puts "#{sender},#{receiver},#{flags}"
