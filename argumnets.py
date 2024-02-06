import argparse

def main():
  parser = argparse.ArgumentParser(description = 'Parse string, int, and float arguments.')
  
  parser.add_argument('input_string', type = str, help = 'Input String')
  parser.add_argument('input_string', type = int, help = 'Input Integer')
  parser.add_argument('input_float', type = float, help = 'Input Float')

  args = parser.parse_args()

  print('String:', args.input_string)
  print('Integer:', args.input_int)
  print('Float:', args.input_float)

if __name__ = "__main__":
  main()
    
