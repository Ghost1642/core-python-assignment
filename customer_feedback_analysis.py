def positive_feedback_percentage(ratings):
    if not ratings:
        return "No ratings available"
    positive=len([r for r in ratings if r>=4])
    return f"Positive Feedback: {(positive/len(ratings))*100}%"
ratings=[5,4,3,5,2,4,1,5]
print(positive_feedback_percentage(ratings))
