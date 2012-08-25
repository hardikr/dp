#!/usr/bin/env ruby
# http://www.reddit.com/r/dailyprogrammer/comments/yqydh/8242012_challenge_91_easy_sleep_sort/

ARGV.map { |n| 
  Thread.new do 
    sleep(n.to_i) 
    puts(n) 
  end
}
.each { |t| 
  t.join
}