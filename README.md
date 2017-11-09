# Brainf_ck compiler to GoLang

## Generate the *.go* file

First install the required dependecies for this project:  
`pip install -r requirements.txt`

To generate the *.go* file use:  
`python3 go_fck_compiler.py <input.bf> -o <output.go>  `  
  
__PS:__ This compiler was created using python3.

## Installing Go on Linux
To run the generated file you need Go installed. If you don't have, follow those steps.  

First download the binary release, you can find it [here](https://golang.org/dl/).  
After you've download the file, run:  
`tar -C /usr/local -xzf go1.9.2.linux-amd64.tar.gz`

And then add it to your *.bashrc*:  
`export PATH=$PATH:/usr/local/go/bin`

Verify the successful installation:  
`go version`

## Running *.go* file
So after the Go installed, you could run:  
`go run <output.o>`
  
## Developer
Universidade de Brasília - UnB  
Fundamentos de Compiladores - 2/2017  
**Hugo Neves de Carvalho** - 15/0011792

![logo](http://natebrennand.github.io/concurrency_and_golang/pics/gopher_head.png)
