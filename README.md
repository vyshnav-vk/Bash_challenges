# new-repo
BI0S Pentest


1.
( a.) Display the path of your current directory
( b.) List out the contents of your current directory
( c.) List out the contents of your current directory including hidden files
ans:
  pwd command:used to display the current working directory.
  ls command:to list out the contents in the directory.
  ls -a command: list out all the contents including hidden files in the directory.
  ![image](https://user-images.githubusercontent.com/113587483/226168578-2fe9414a-6a66-4140-92c8-ff13ca25a70a.png)
  
  
2.
( a.) Create a new directory named a
( b.) Move to the newly created directory a 
( c.) Create a blank file named “file1”
( d.) Display the file type of “file1”
( e.) Add the line “Hello World” to “file1” using the command echo
( f.) Display the contents of “file1”
( g.) Display the file type of “file1” again
ans:
  mkdir command:to create a new directory.
  cd directory_name:to move to the repective file.
  touch file_name:to create an empty file.
  file file_name:to display the type of the file.
  echo "Hello World" >> file1.txt command to write to the file.
  cat command:to display the contents of the file.
  ![image](https://user-images.githubusercontent.com/113587483/226169446-8e444f2d-44bc-4007-93de-5444b8c45609.png)
  
  
3.
( a.) Stay in directory a. Create a file “file2” and add the contents below using the  command cat
First Line Second Line Third Line
( b.) Display the contents of “file2”
( c.) Display the contents of “file2” with the lines reversed
ans:
  cat > file2.txt
First Line
Second Line
Third Line
  cat file_name command for displaying the contents
  tac file_name command for displaying the lines in the reverse order.
  ![image](https://user-images.githubusercontent.com/113587483/226170003-94a4797a-5ff7-42fc-a7b3-67bb998d80e6.png)
  
  
4.
( a.) Stay in directory a. Concatenate the contents of “file1” and “file2” and save them into a new file “file3”
( b.) Display the contents of “file3”
ans:
  cat file1.txt file2.txt > file3.txt command to concatenate the contents of file1 and file2 to a new file file3
  cat file_name to display the contents of the file.
  ![image](https://user-images.githubusercontent.com/113587483/226170307-1b087094-70d1-4c27-a169-d84e6ffe0b7a.png)
  
  
5.
( a.) Stay in directory a. Create 2 directories b/c with a single command 
( b.) Create a new directory d
( c.) Copy the directory d to directory c using a single command
( d.) Delete the directory d in the current directory a
( e.) Copy “file3” to the directory d with a single command
ans:
  mkdir dir1 dir2 command to create two directories in a single command.
  mkdir dir_name:to create a directory
  cp -r dir1 dir2 command to copy dir1 and all its contents to dir2.
  rmdir dir_name to delete a directory.
  cp filename dir_name commad copy the file to the respective directory.
  ![image](https://user-images.githubusercontent.com/113587483/226170997-fb7fe160-465a-4419-84c3-be4313c519d5.png)
  
  
6.
( a.) Go to directory d and rename “file3” to “file0”
( b.) Stay in the same directory and move “file0” to directory a
ans:
  mv file_name new_file_name:renames the old file with new file name.
  mv filename dir:moves the file to the respective directory.
  ![image](https://user-images.githubusercontent.com/113587483/226172493-45d920c8-87d4-463d-8b1c-c637a74d44c8.png)
  
  
7.
( a.) Go to your home directory
( b.) Create a file named “test” in the directory a/b/c/d
( c.) Stay in the home directory. Find and display the path of “test”
ans:
  cd command with no file name will direct to the home directory.
  touch command will create a file in the specified directory.eg,touch a/test will create a file named test in directory a.
  find /-name file_name will find the path of the given file.
  ![image](https://user-images.githubusercontent.com/113587483/226173396-9e59dda8-b9ee-4a6a-bf29-e326a1ad9027.png)
  ![image](https://user-images.githubusercontent.com/113587483/226173437-c5aa6dc3-cde7-4b8c-96a3-3567f84222fe.png)
  ![image](https://user-images.githubusercontent.com/113587483/226173459-9cb98267-c582-4f5c-8209-7d66b8b085ea.png)
  
  
8.
( a.) Go to directory a. Get the man page of grep and save its contents to a file named “grepman.txt”
( b.) Print the lines containing the word “FILE” (Case sensitive) in the file “grepman.txt”
ans:
  using cd command we go to the required directory.And then using the command man grep > file_name, we store the contents of man page in the required file.
  using grep command. grep 'FILE' grepman.txt
  ![image](https://user-images.githubusercontent.com/113587483/226173944-c448305a-71f4-402d-b1ba-2d2b3207961b.png)
  
  
9.
( a.) Go to directory a and remove the directory b with a single command
( b.) Remove the files starting with the word “file” with a single command
ans:
  usind cd command go to directory a and then using the rmdir command remove directory b.
  using the command rm file* will delete all the files that start with the word file.
  ![image](https://user-images.githubusercontent.com/113587483/226174374-3689eaf9-2895-456a-908c-62a184eef097.png)
  
  
10.
( a.) Download the compressed file from the drive. https://drive.google.com/drive/folders/1PG3ZlpFu6nQSNjpCNuceoGcNey00bhPP?usp=sharing
( b.) Extract the compressed file using CLI. 
( c.) Decode the base64 content and display the content of “Flag.txt”using CLI.
ans:
  extraction using tar -zxvf file_name.tar.gz
  ![image](https://user-images.githubusercontent.com/113587483/226174861-d42cbedf-54c2-415c-910c-03ad3c145580.png)
  decoding using the command base64 -dencoded_file_name > decoded_file_name.
  Flag: You Found The Flag.
  ![image](https://user-images.githubusercontent.com/113587483/226175489-bcc48754-f7d6-41c2-b595-efcfb0947b69.png)

  

  




  

