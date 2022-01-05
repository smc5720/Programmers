function solution(a, b) {
    let month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    let total = b;
    
    for (let i = 0; i < a; i++) {
        total += month[i];
    }
    
    return day[total % 7];
}