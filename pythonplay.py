string = """To design and implement the user review techonoloy in the podcast and playlist the developers will not need to do anything new. The technology is already being utilised else where in the software so no new technology needs to be implemented. Add-ons are required to existing infrustructer. To begin the project the manager will need to chat requirements with maybe a UX-UI designer to design the layout of the review chat boxes. Once the layout has been designed the two teams of front-end and back-end will split off and implement the add-on architecture with the manager running the devops. There will be on-going testing and monitoring.

To design and implement the Song matching technology similar to shazam may be difficult. To ensure that they are not accused of interlectual theft they will need to design the technology themselves or find an open-source technology. I assume that if they were to design it themselves that they might need a computer-science engineer or electrical engineer to monitor the signal an to transform the signal into something a computer understands. In the updated ERD diagram in R8 I assumed the signal may be picked up by a microphone and decoded into binary somehow. Once the signal can be converted the rest can be left up to the dev teams.

To design and implement the analytical monitoring of the user designed podcast and give feedback I would consider a machine learning algorithm. It most likely will be designed by a computer-science engineer or statician that can work in parallel with such technologies as google analytics or similar. The algorithm will assess what all the favourite podcasts will have as far as themes, character, tone, topics, categories and compare that to the user's current technologies. I expect there may be a degree of difficulty with dev ops. I assume there will be many prototypes and monitoring of bugs. 


#### How the improvement will effect stakeholders who utilise the system



#### Additional cost that may be incurred to implement the improvement

Adding a review comments section in the spotify app will be quick and simple. So operations cost will be as cheap as any simple update or patch. Though there will be an ongoing expanse.  More data will need to be stored. So Spotify will either have to raise prices for the extra feature or have a loss to revenue. 

The additional cost for the song and voice matching technology may be expensive depending if the technology needs to be designed or found on open source. Also Spotify could offer a payment to buy the technology which could be very expensive also. There will definitly be additional cost in storing the extra data required to match 50 million songs. There might be extra cost in processing power to analyse the signals but neglible on the scale of spotify.

The analytical monitoring technology may be expensive short term. I dont believe that there will be expensive ongoing fees. The analytical data is already being collected. So short term will just be designing and implementing the algorithm with the engineers and dev ops."""
string_list = string.split(" ")
print(len(string_list))