from selectorlib import Extractor
import requests 
import json
import argparse
from pythonosc import udp_client
from pythonosc import osc_message_builder
import locale


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=9001,
      help="The port the OSC server is listening on")

  parser.add_argument('-u', "--url", help='Amazon Product Url in -> ""', required=True)
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  # Create an Extractor by reading from the YAML file
  e = Extractor.from_yaml_file('selectors.yml')

  #change user agent if amazon detect you as a robot
  #Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
  user_agent = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
  headers = {'User-Agent': user_agent}

  r = requests.get(args.url, headers=headers)
  #print(r.text) debug
  # Pass the HTML of the page and create 
  data = e.extract(r.text)
  # Print the data for debug
  #print(json.dumps(data, indent=True))#debug

  locale.setlocale(locale.LC_ALL, 'it_IT.UTF8')
  notAvailable = False

  #calculate sell price
  money1 = data["SalePrice"]
  if not money1:#product not available
    notAvailable = True
    discountPercentage = 0
  else:
    salePrice = locale.atof(money1.strip("€")) #strip() remove characters from the string #locale.atof() convert a string in float
    print ("Sale Price: ", salePrice)

    #calculate original price
    money2 = data["OriginalPrice"]
    if not money2:#if money is empty    
      originalPrice = salePrice
    else:
      originalPrice = locale.atof(money2.strip("€"))
      print ("Original Price:", originalPrice)

    discountPercentage = 100 -(salePrice*100/originalPrice)

  if notAvailable:
    print("Product not available")
  #else:
    #print("Discount Percentage: ", discountPercentage)

  #notAvailable product
  if notAvailable:
    msg = osc_message_builder.OscMessageBuilder(address = '/test/voice')
    msg.add_arg(60, arg_type='f')
    msg.add_arg(80, arg_type='f')
    msg.add_arg(20, arg_type='f')
    msg = msg.build()
    client.send(msg)

  elif discountPercentage < 5 :
    msg = osc_message_builder.OscMessageBuilder(address = '/test/voice')
    msg.add_arg(65, arg_type='f')
    msg.add_arg(65, arg_type='f')
    msg.add_arg(0, arg_type='f')
    msg = msg.build()
    client.send(msg)

  elif discountPercentage < 10 :
    msg = osc_message_builder.OscMessageBuilder(address = '/test/voice')
    msg.add_arg(68, arg_type='f')
    msg.add_arg(75, arg_type='f')
    msg.add_arg(2, arg_type='f')
    msg = msg.build()
    client.send(msg)

  elif discountPercentage < 20 :
    msg = osc_message_builder.OscMessageBuilder(address = '/test/voice')
    msg.add_arg(70, arg_type='f')
    msg.add_arg(85, arg_type='f')
    msg.add_arg(6, arg_type='f')
    msg = msg.build()
    client.send(msg)

  elif discountPercentage < 25 :
    msg = osc_message_builder.OscMessageBuilder(address = '/test/voice')
    msg.add_arg(72, arg_type='f')
    msg.add_arg(90, arg_type='f')
    msg.add_arg(10, arg_type='f')
    msg = msg.build()
    client.send(msg)
  
  elif discountPercentage < 30 :
    msg = osc_message_builder.OscMessageBuilder(address = '/test/voice')
    msg.add_arg(75, arg_type='f')
    msg.add_arg(92, arg_type='f')
    msg.add_arg(13, arg_type='f')
    msg = msg.build()
    client.send(msg)

  else :
    msg = osc_message_builder.OscMessageBuilder(address = '/test/voice')
    msg.add_arg(77, arg_type='f')
    msg.add_arg(100, arg_type='f')
    msg.add_arg(18, arg_type='f')
    msg = msg.build()
    client.send(msg)
