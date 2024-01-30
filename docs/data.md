# Data

## Sources

- On The Issues: web repository for candidate quotes by position
- Wikipedia: Candidate and party profiles and political positions (when available for the candidate)

### On The Issues

- Their data seems to be relatively standard. I used a separate parser with BS4 to scrape the text data from the site until I got throttled and had to copy past by hand. It could have been my internet connection.
- Regardless, I like how I captured it. Seems like a statement first, then the supporting quote/content and then a source reference. The source looks like it is consistently labeled so that will be my split point for the regex.
- After source, first line is inconsistently punctuated and inconsistently labeled, if labeled at all now that i look at it more.
  
  - 1st line end at new line, label as 'Statement'
  - Between that new line and the new line prior to 'source:', should be our quote content, label as 'Content'
  - Source is final in record and label as 'Source'

### Wikipedia

- Party History
- Party Positions
- Individual candidate articles
- Individual candidate policy positions
