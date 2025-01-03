use std::fs;

fn main() {
    let file_path = "input.txt";

    let contents = fs::read_to_string(file_path)
        .expect("Should have read the input!");
    
    let str_contents = contents.as_str();

        //println!("With text:\n{contents}");
    let numbers = str_contents.split("\n").split(" ");
    
    for num in numbers {
        println!("Number is {num}");
    }
}
