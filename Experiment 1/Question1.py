#write a program to remove a set of stop words from a paragraph
stop_words_string = '. , a they the his so and were from that of in only with to'
stop_words = stop_words_string.split()
print(stop_words)

paragraph = "Ronaldo made his senior international debut for Portugal in 2003 at age 18 , and has since earned 170 caps , including appearing and scoring in ten major tournaments , becoming Portugal's most capped player and his country's all-time top goalscorer. He scored his first international goal at Euro 2004 where he helped Portugal reach the final and assumed full captaincy of the national team in July 2008. In 2015 Ronaldo was named the best Portuguese player of all time by the Portuguese Football Federation. The following year he led Portugal to their first triumph in a major tournament by winning Euro 2016, and received the Silver Boot as the second-highest goalscorer of the tournament."
result = ""
paragraph = paragraph.split()
for word in paragraph:
  if word not in stop_words:
    result = result + word + " "
print(result)
