art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%


'''                               

encoded_values = [] # Declared this up here so it can be passed to both of the below functions                                                             

def encodeString(ascii_art):
    previous_value = ascii_art[0]
    count = 0 # Iterator!
    for char in ascii_art:
        if char != previous_value: # Check if the current character and the previous character do NOT match
            encoded_values.append((previous_value, count)) # If that's the case, append the previous character and the number of times it's repeated as a tuple to the list of encoded values
            count = 0 # Reset the counter for every iteration. The count would keep going up if you didn't include this!
        previous_value = char # After the if clause is satisfied, set the current character as the previous value, then continue to the next character in the ASCII art
        count = count + 1 # Also works with count += 1, but this is more readable. I used the latter in the decode function.
    encoded_values.append((previous_value, count))

    return encoded_values
    

'''def decodeString(encodedList):
    decoded_string = ""
    count = 0
    for tup in encodedList:
      tup = str([char[0] for char in encoded_values])

      decoded_string = tup * count

      count += 1

    return decoded_string''' # I was WAY off on this one.


# This is the correct decodeString function, lifted from the LinkedIn Learning course:
def decodeString(encodedList):
  decoded_string = ""
  for char in encodedList: # Get each value from the list of encoded values (for instance, encoded_values[0] = (\n, 2))
    decoded_string = decoded_string + char[0] * char[1] # Append the *first* value in each tuple to decoded_string, then repeat it by multiplying that character by the second value in the tuple.

  return decoded_string # And this works! See how I was overthinking it in the above attempt?

print(encodeString(art))
print(decodeString(encoded_values))