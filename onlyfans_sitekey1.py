
import capsolver
import requests

# Consider using environment variables for sensitive information
PROXY = "http://username:password@ip:port"
capsolver.api_key = ""
PAGE_URL = "https://onlyfans.com/"
PAGE_KEY = "314ec50a-c08a-4c0a-a5c4-4ed4c7ed5aff"

def solve_hcaptcha(url,key):
    solution = capsolver.solve({
        "type": "HCaptchaTask",
        "websiteURL": url,
        "websiteKey":key,
        "proxy": PROXY
    })
    return solution

def main():
 
    
    print("Solving hCaptcha...")
    solution = solve_hcaptcha(PAGE_URL, PAGE_KEY)
    print("Solution: ", solution)

if __name__ == "__main__":
    main()
