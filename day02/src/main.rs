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
    Ok(())
}
