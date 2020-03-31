-------------------------------------------------------------

### DISPLAY INFORMATION

-------------------------------------------------------------

> #### void disp ( object )
> this function displays a stringified object to the standard output.
> - **@parameter** : object - any variable that can be converted into  string
> - **@return**    : N/A

> #### void debug ( object )
> this function displays a stringified object to the standard error.
> If the object is a list, it displays each entry on a new single line.
> - **@parameter** : object - any variable that can be converted into  string
> - **@return**    : N/A

-------------------------------------------------------------

#### INPUT FUNCTIONS

-------------------------------------------------------------

> ### list\<int\> | int getInt ( int n=1 )
> Returns a simple integer value from the stdin.
> It can return a list of integers from the stdin (each float value is on a different line).  
> The 'n' (optional) parameter is strictly positive, and represents the count of lines to retrieve.
> If 'n' equals to '1' (default value), the result is a simple integer. If greater than 1 (compulsory parameter), the result is an integer list.  
> - **@parameter** : n - optional positive parameter with default value to 1
> - **@return**    : integer value (if n equals to 1)
> - **@return**    : integer  list (if n greater than 1)

> ### list\<float\> | float getFloat ( string coma=".", int n=1 )
> Returns a simple float value from the stdin.
> It can return a list of floats from the stdin (each float value is on a different line).  
> This function takes the coma character in order to be able to replace it before convertion.  
> The 'n' (optional) parameter is strictly positive, and represents the count of lines to retrieve.
> If 'n' equals to '1' (default value), the result is a simple float. If greater than 1 (compulsory parameter), the result is a float list.  
> - **@parameter** : coma - optional string parameter with default value to "."
> - **@parameter** : n - optional positive parameter with default value to 1
> - **@return**    : float value (if n equals to 1)
> - **@return**    : float list (if n greater than 1)


 
 


