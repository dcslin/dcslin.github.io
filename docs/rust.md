# Rust lang

## Basic Syntax

```rust
fn main() {
    const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;

    let mut x = 5;
    println!("x is {x}");
    x = 6;
    println!("x is {x}");

    let guess:u32 = "42".parse().expect("failed to parse")

    let x = 2.0; // f64

    let y: f32 = 3.0; // f32

    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;

    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;

    let a = [1, 2, 3, 4, 5];

    let a: [i32; 5] = [1, 2, 3, 4, 5];

    let a = [3; 5];

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }

    let number = if condition { 5 } else { 6 };

    loop {
        println!("again!");
        break;
    }

    while number != 0 {
        println!("{number}!");

        number -= 1;
    }

    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }

    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("LIFTOFF!!!");
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}

fn five() -> i32 {
    5
}

```

## Primitive Types, Collections

string, tuple, vector

```rust
let s = "hello";

let s = String::from("hello");
```


`String` vs `".."` vs `str`

`&str` is `&s[..]` string slice.
`String` is string object. 
`".."` is string literal.

## Unique Concepts

Ownership, Reference, borrowing, pattern matching, Stack and Heap, Result and Panic, Traits, Lifetimes, smart pointers

Move 

```
    let x = 5;
    let y = x;

    let s1 = String::from("hello");
    let s2 = s1;
```

```
fn takes_and_gives_back(a_string: String) -> String { // a_string comes into
    a_string  // a_string is returned and moves out to the calling function
}
```

Reference/borrowing

```
fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{s1}' is {len}.");
}

fn calculate_length(s: &String) -> usize {
    s.len()
}

fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

slice Reference
```
    let s = String::from("hello world");

    let hello = &s[0..5];
    let world = &s[6..11];
```

Slice ref type, `&[i32]`

enum

```
    enum IpAddrKind {
        V4,
        V6,
    }

    struct IpAddr {
        kind: IpAddrKind,
        address: String,
    }

    let home = IpAddr {
        kind: IpAddrKind::V4,
        address: String::from("127.0.0.1"),
    };

    let loopback = IpAddr {
        kind: IpAddrKind::V6,
        address: String::from("::1"),
    };
```

match
```
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
fn main(){
    fn plus_one(x: Option<i32>) -> Option<i32> {
        match x {
            None => None,
            Some(i) => Some(i + 1),
        }
    }

    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);
}
```

```
    let mut count = 0;
    if let Coin::Quarter(state) = coin {
        println!("State quarter from {state:?}!");
    } else {
        count += 1;
    }
```

Result

```
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the file: {error:?}"),
    };
}
```

return result error directly

```
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
```

## Other Core Concepts

Generics, enum, Closures, Iterators, struct, threading, oop

struct

```
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );
}

```

## Build Tools
Cargo, workspace, project structure, tests

```sh
cargo new project0

cargo build

cargo run


```


workspace

Filename: Cargo.toml
```
[workspace]

members = [
    "adder",
    "add_one",
]
```

```
cargo new adder

cargo new add_one --lib
```

Filename: adder/Cargo.toml
```
[dependencies]
add_one = { path = "../add_one" }
```

## Tests

```
pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
```