require 'pi_piper'
include PiPiper

led = Pin.new(pin: 17, direction: :out)

loop do
  led.on
  sleep 1
  led.off
end

