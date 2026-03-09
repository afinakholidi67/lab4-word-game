REM Simple song in BASIC - prints lyrics and attempts to play a melody
CLS
PRINT "Simple BASIC Song"
PRINT
PRINT "Verse 1:"
PRINT "I learn to code in BASIC, beep and tune we play"
PRINT "On tiny screens and ancient chips, we practice every day"
PRINT
REM The following PLAY line works in QBasic/QuickBASIC/FreeBASIC (if supported)
REM Tempo T120, octave O4, short note length L8
PLAY "T120 O4 L8 E E F G G F E D C C D E G"

REM Short pause loop (simple timing when PLAY is not available)
FOR I = 1 TO 200: NEXT I

PRINT
PRINT "Chorus:"
PRINT "Beep and boop, the BASIC tune, in loops we run along"
PRINT "Lines of code and simple notes make up this silly song"

REM Repeat melody
PLAY "T120 O4 L8 G G A A G F E D C"
FOR I = 1 TO 200: NEXT I

PRINT "-- End of song --"
END
