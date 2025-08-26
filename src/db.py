import psycopg2

def save_transcript(call_id, transcript):
    conn = psycopg2.connect('postgresql://localhost/vocamind')
    cur = conn.cursor()
    cur.execute('INSERT INTO transcripts (call_id, text) VALUES (%s, %s)', (call_id, transcript))
    conn.commit()
    cur.close()
    conn.close()
