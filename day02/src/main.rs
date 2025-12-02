use std::error::Error;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn part1(ranges: &Vec<(u64, u64)>) -> u64 {
    let mut sum = 0;
    for range in ranges.iter() {
        let (first, last) = range;
        for i in *first..=*last {
            let modulo: u64 = match i {
                10..=99 => 11,
                1000..=9999 => 101,
                100000..=999999 => 1001,
                10000000..=99999999 => 10001,
                1000000000..=9999999999 => 100001,
                100000000000..=999999999999 => 1000001,
                10000000000000..=99999999999999 => 10000001,
                1000000000000000..=9999999999999999 => 100000001,
                100000000000000000..=999999999999999999 => 1000000001,
                10000000000000000000..=u64::MAX => 10000000001,
                _ => { continue; }
            };
            if i % modulo == 0 {
                sum += i;
            }
        }
    }
    sum
}

fn part2(ranges: &Vec<(u64, u64)>) -> u64 {
    let mut sum = 0;
    for range in ranges.iter() {
        let (first, last) = range;
        for i in *first..=*last {
            match i {
                10..=99 => {
                    if i % 11 == 0 {
                        sum += i;
                    }
                }
                100..=999 => {
                    if i % 111 == 0 {
                        sum += i;
                    }
                }
                1000..=9999 => {
                    if i % 101 == 0 {
                        sum += i;
                    }
                }
                10000..=99999 => {
                    if i % 11111 == 0 {
                        sum += i;
                    }
                }
                100000..=999999 => {
                    if i % 1001 == 0 || i % 10101 == 0 {
                        sum += i;
                    }
                }
                1000000..=9999999 => {
                    if i % 1111111 == 0 {
                        sum += i;
                    }
                }
                10000000..=99999999 => {
                    if i % 10001 == 0 || i % 1010101 == 0 {
                        sum += i;
                    }
                }
                100000000..=999999999 => {
                    if i % 1001001 == 0 {
                        sum += i;
                    }
                }
                1000000000..=9999999999 => {
                    if i % 100001 == 0 || i % 101010101 == 0 {
                        sum += i;
                    }
                }
                10000000000..=99999999999 => {
                    if i % 11111111111 == 0 {
                        sum += i;
                    }
                }
                100000000000..=999999999999 => {
                    if i % 1000001 == 0 || i % 100010001 == 0 || i % 1001001001 == 0 || i % 10101010101 == 0 {
                        sum += i;
                    }
                }
                1000000000000..=9999999999999 => {
                    if i % 1111111111111 == 0 {
                        sum += i;
                    }
                }
                10000000000000..=99999999999999 => {
                    if i % 10000001 == 0 || i % 1010101010101 == 0 {
                        sum += i;
                    }
                }
                100000000000000..=999999999999999 => {
                    if i % 10000100001 == 0 || i % 1001001001001 == 0 {
                        sum += i;
                    }
                }
                1000000000000000..=9999999999999999 => {
                    if i % 100000001 == 0 || i % 1000100010001 == 0 || i % 101010101010101 == 0 {
                        sum += i;
                    }
                }
                10000000000000000..=99999999999999999 => {
                    if i % 11111111111111111 == 0 {
                        sum += i;
                    }
                }
                100000000000000000..=999999999999999999 => {
                    if i % 1000000001 == 0 || i % 1000001000001 == 0 || i % 1001001001001001 == 0 || i % 10101010101010101 == 0 {
                        sum += i;
                    }
                }
                1000000000000000000..=9999999999999999999 => {
                    if i % 1111111111111111111 == 0 {
                        sum += i;
                    }
                }
                10000000000000000000..=u64::MAX => {
                    if i % 10000000001 == 0 || i % 1000010000100001 == 0 || i % 10001000100010001 == 0 || i % 1010101010101010101 == 0 {
                        sum += i;
                    }
                }
                _ => { continue; }
            };
        }
    }
    sum
}

fn main() -> Result<(), Box<dyn Error>> {
    let input_file = File::open("input")?;
    let mut reader = BufReader::new(input_file);
    let mut buf = vec![];
    let mut ranges = vec![];
    while reader.read_until(b',', &mut buf)? > 0 {
        if buf.last() == Some(&b',') || buf.last() == Some(&b'\n') {
            buf.pop();
        }
        let this_buf = buf.split_off(0);
        let dash_index = this_buf.iter().position(|c| c == &b'-').ok_or("no '-' found")?;
        let (num1, num2) = this_buf.split_at(dash_index);
        let num1: u64 = String::from_utf8(num1.to_vec())?.parse()?;
        let num2: u64 = String::from_utf8(num2[1..].to_vec())?.parse()?;
        ranges.push((num1, num2));
    }

    println!("part 1: {}", part1(&ranges));
    println!("part 2: {}", part2(&ranges));
    Ok(())
}
