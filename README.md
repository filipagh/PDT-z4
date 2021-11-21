### autor: Filip Agh
### git: https://github.com/filipagh/PDT-z4

# uloha 1

### embeding

hastagy tweetov si ulozim priamo v doc tweetu

nema zmysel ich ukladat mimo na zaklade poziadaviek

### referencie
tweet bude mat referenciu na autora

je zbytocne mat duplicitne vsetky udaje o autorovi v kazdom jeho tweete, nehovoriac o ich updatovani

### account
| \_id | description | followers\_count | friends\_count | id | name | screen\_name | statuses\_count |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 619a81cf59d694f699ad5f57 | Voice of Polish patriotic Biblical Christians. 100% independent viewer funded, uncensored news from Poland. #FollowJesus 🇵🇱🇺🇸🇮🇱 #KAG #PolesForTrump2020 | 5491 | 5510 | 950734466909200384 | Against the Tide \(Idź Pod Prąd\) TV | AgainstTideTV | 5118 |


### tweet

| \_id | account\_id | content | happened\_at | hastagas | id | parent\_id |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 619a81d059d694f699ad5f59 | 619a81cf59d694f699ad5f57 | This is a war, China's worse than Soviet Russia. #BoycottChina  and #MakeChinaPay #ChinaLiedPeopleDied - @SolomonYue @GOPOverseasHK #ccot #pjnet https://t.co/s2K9frLp2S<br/>SIGN the Petition<br/>https://t.co/YwyB7tRDCw @realDonaldTrump @VP @SecPompeo @parscale @DanScavino @EricTrump https://t.co/H7KLBUlxAY | 2020-04-05T18:55:12.000Z | \["BoycottChina", "ccot", "ChinaLiedPeopleDied", "MakeChinaPay", "pjnet"\] | 1246874043682299904 | NULL |





# uloha 2
vid py package

importuju sa tweety a ucty

# uloha 3

#### cast A.

```
db.getSiblingDB("PDT").getCollection("tweets").aggregate([
       {
         $project: {"t": "$$ROOT", "_id": 0}
       },
       {
         $lookup: {
           localField: "t.account_id",
           from: "accounts",
           foreignField: "_id",
           as: "a"
         }
       },
       {
         $unwind: {
           path: "$a",
           preserveNullAndEmptyArrays: false
         }
       },
       {
         $match: {"a.screen_name": {$eq: 'Marndin12'}}
       },
       {
         $sort: {"t.happened_at": -1}
       },
       {
         $replaceRoot: {
           newRoot: {$mergeObjects: ["$a", "$t", "$$ROOT"]}
         }
       },
       {
         $project: {"a": 0, "t": 0}
       },
       {
         $limit: 10
       }
     ])

```
| \_id | account\_id | content | description | followers\_count | friends\_count | happened\_at | hastagas | id | name | parent\_id | screen\_name | statuses\_count |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 619a871c4375e67831611449 | 619a86ff4375e678316113e7 | @End\_TheFederalR Here's a three minute pop song that describes what life could actually be like for the survivors of agenda 21/2030. https://t.co/8F3GRJBy3e #agenda21 #agenda2030 #coronavirus #event201 | https://t.co/lIHnBiqfls<br/>https://t.co/HOA3RgtAc9… | 1107 | 957 | 2020-02-11T19:47:09.000Z | \["agenda2030", "agenda21", "coronavirus", "event201"\] | 1227318173789233153 | Martin Noakes | NULL | Marndin12 | 18755 |
| 619a871b4375e67831611447 | 619a86ff4375e678316113e7 | @Berean122 @eath1223 Actually 1968 - Here's a 3 minute pop song that describes what life could actually be like for the survivors of agenda 2030. IMHO, this is what the elite have planned for us unless we wake up and resist - https://t.co/8F3GRJBy3e #agenda21 #agenda2030 #coronavirus #event201 | https://t.co/lIHnBiqfls<br/>https://t.co/HOA3RgtAc9… | 1107 | 957 | 2020-02-09T12:45:24.000Z | \["agenda2030", "agenda21", "coronavirus", "event201"\] | 1226487259274399744 | Martin Noakes | NULL | Marndin12 | 18755 |
| 619a871b4375e67831611445 | 619a86ff4375e678316113e7 | @4Mina Hi there - Here's a 3 minute pop song that describes what life could actually be like for the survivors of agenda 2030. IMHO, this is what the elite have planned for us unless we wake up and resist - https://t.co/8F3GRJBy3e #agenda21 #agenda2030 #coronavirus #event201 | https://t.co/lIHnBiqfls<br/>https://t.co/HOA3RgtAc9… | 1107 | 957 | 2020-02-09T12:44:51.000Z | \["agenda2030", "agenda21", "coronavirus", "event201"\] | 1226487122812690433 | Martin Noakes | NULL | Marndin12 | 18755 |
| 619a871a4375e67831611443 | 619a86ff4375e678316113e7 | @talk2melodie Here's a 3 minute pop song that describes what life could actually be like for the survivors of agenda 2030. IMHO, this is what the elite have planned for us unless we wake up and resist - https://t.co/8F3GRJBy3e #agenda21 #agenda2030 #coronavirus #event201 | https://t.co/lIHnBiqfls<br/>https://t.co/HOA3RgtAc9… | 1107 | 957 | 2020-02-09T12:43:44.000Z | \["agenda2030", "agenda21", "coronavirus", "event201"\] | 1226486841978839040 | Martin Noakes | NULL | Marndin12 | 18755 |
| 619a873f4375e678316114b9 | 619a86ff4375e678316113e7 | @CoZza\_86 Hi - Here's a 3 minute pop song that describes what life could actually be like for the survivors of agenda 2030. IMHO, this is what the elite have planned for us unless we wake up and resist - https://t.co/8F3GRJBy3e #agenda21 #agenda2030 #coronavirus #event201 | https://t.co/lIHnBiqfls<br/>https://t.co/HOA3RgtAc9… | 1107 | 957 | 2020-02-09T12:42:41.000Z | \["agenda2030", "agenda21", "coronavirus", "event201"\] | 1226486574738743296 | Martin Noakes | NULL | Marndin12 | 18755 |
| 619a871a4375e67831611441 | 619a86ff4375e678316113e7 | @JohnPar27202430 @YouTube Hi John - Agenda 2030 explained in a 3 minute song I believe this is what the elite have planned for us all unless we wake up and resist - https://t.co/8F3GRJBy3e  #agenda21 #agenda2030 #coronavirus #event201 | https://t.co/lIHnBiqfls<br/>https://t.co/HOA3RgtAc9… | 1107 | 957 | 2020-01-31T18:00:35.000Z | \["agenda2030", "agenda21", "coronavirus", "event201"\] | 1223305087658942472 | Martin Noakes | NULL | Marndin12 | 18755 |
| 619a87194375e6783161143f | 619a86ff4375e678316113e7 | @AnnMarieCopla10 @adverbjunkie @TomJChicago Hi Anne - Agenda 2030 explained in a 3 minute song I believe this is what the elite have planned for us all unless we wake up and resist - https://t.co/8F3GRJBy3e  #agenda21 #agenda2030 #coronavirus #event201 | https://t.co/lIHnBiqfls<br/>https://t.co/HOA3RgtAc9… | 1107 | 957 | 2020-01-31T18:00:04.000Z | \["agenda2030", "agenda21", "coronavirus", "event201"\] | 1223304957312585728 | Martin Noakes | NULL | Marndin12 | 18755 |
| 619a87184375e6783161143d | 619a86ff4375e678316113e7 | @dogsrockatx @OldSchool2A @POTUS \*\*Agenda 2030 explained in a 3 minute song I believe this is what the elite have planned for us all unless we wake up and resist - https://t.co/8F3GRJBy3e  #agenda21 #agenda2030 #coronavirus #event201 | https://t.co/lIHnBiqfls<br/>https://t.co/HOA3RgtAc9… | 1107 | 957 | 2020-01-31T17:30:01.000Z | \["agenda2030", "agenda21", "coronavirus", "event201"\] | 1223297395288682498 | Martin Noakes | NULL | Marndin12 | 18755 |
| 619a873e4375e678316114b7 | 619a86ff4375e678316113e7 | @TimothyMShrops1 @Truckerpea @DanielTurnerPTF @DavidJHarrisJr Timothy - Agenda 2030 explained in a 3 minute song I believe this is what the elite have planned for us all unless we wake up and resist - https://t.co/8F3GRJBy3e  #agenda21 #agenda2030 #coronavirus #event201 Plz Share | https://t.co/lIHnBiqfls<br/>https://t.co/HOA3RgtAc9… | 1107 | 957 | 2020-01-31T17:28:57.000Z | \["agenda2030", "agenda21", "coronavirus", "event201"\] | 1223297125322252289 | Martin Noakes | NULL | Marndin12 | 18755 |
| 619a873d4375e678316114b5 | 619a86ff4375e678316113e7 | @nonsense\_planet Agenda 2030 explained in a 3 minute song I believe this is what the elite have planned for us all unless we wake up and resist - https://t.co/8F3GRJBy3e  #agenda21 #agenda2030 #coronavirus #event201 | https://t.co/lIHnBiqfls<br/>https://t.co/HOA3RgtAc9… | 1107 | 957 | 2020-01-31T17:19:03.000Z | \["agenda2030", "agenda21", "coronavirus", "event201"\] | 1223294637252710400 | Martin Noakes | NULL | Marndin12 | 18755 |

#### cast B.
vstup

| \_id | account\_id | content | happened\_at | hastagas | id | parent\_id |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 619a86edea5f211bfedd9c1a | 619a86ecea5f211bfedd9c18 | This is a war, China's worse than Soviet Russia. #BoycottChina  and #MakeChinaPay #ChinaLiedPeopleDied - @SolomonYue @GOPOverseasHK #ccot #pjnet https://t.co/s2K9frLp2S<br/>SIGN the Petition<br/>https://t.co/YwyB7tRDCw @realDonaldTrump @VP @SecPompeo @parscale @DanScavino @EricTrump https://t.co/H7KLBUlxAY | 2020-04-05T18:55:12.000Z | \["BoycottChina", "ccot", "ChinaLiedPeopleDied", "MakeChinaPay", "pjnet"\] | 1246874043682299904 | NULL |
| 619a86eeea5f211bfedd9c1e | 619a86edea5f211bfedd9c1c | RT @AgainstTideTV: This is a war, China's worse than Soviet Russia. #BoycottChina  and #MakeChinaPay #ChinaLiedPeopleDied - @SolomonYue @GO… | 2020-04-05T21:11:07.000Z | \["BoycottChina", "ChinaLiedPeopleDied", "MakeChinaPay"\] | 1246908249577787393 | 1246874043682299904 |
| 619a86eeea5f211bfedd9c22 | 619a86eeea5f211bfedd9c20 | RT @AgainstTideTV: This is a war, China's worse than Soviet Russia. #BoycottChina  and #MakeChinaPay #ChinaLiedPeopleDied - @SolomonYue @GO… | 2020-04-06T10:28:53.000Z | \["BoycottChina", "ChinaLiedPeopleDied", "MakeChinaPay"\] | 1247109014694932481 | 1246874043682299904 |


query:
```
db.getSiblingDB("PDT").getCollection("tweets").aggregate([
       {
         $project: {"t": "$$ROOT", "_id": 0}
       },
       {
         $lookup: {
           localField: "t.account_id",
           from: "accounts",
           foreignField: "_id",
           as: "a"
         }
       },
       {
         $unwind: {
           path: "$a",
           preserveNullAndEmptyArrays: false
         }
       },
       {
         $match: {"t.parent_id": {$eq: '1246874043682299904'}}
       },
       {
         $project: {"_id": "$t._id", "happened_at": "$t.happened_at", "id": "$t.id", "content": "$t.content", "hastagas": "$t.hastagas", "screen_name": "$a.screen_name"}
       },
       {
         $limit: 10
       }
     ])
[2021-11-21 23:58:40] 2 rows retrieved starting from 1 in 329 ms (execution: 315 ms, fetching: 14 ms)

```


| \_id | content | happened\_at | hastagas | id | screen\_name |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 619a86eeea5f211bfedd9c1e | RT @AgainstTideTV: This is a war, China's worse than Soviet Russia. #BoycottChina  and #MakeChinaPay #ChinaLiedPeopleDied - @SolomonYue @GO… | 2020-04-05T21:11:07.000Z | \["BoycottChina", "ChinaLiedPeopleDied", "MakeChinaPay"\] | 1246908249577787393 | ZawdzkiP |
| 619a86eeea5f211bfedd9c22 | RT @AgainstTideTV: This is a war, China's worse than Soviet Russia. #BoycottChina  and #MakeChinaPay #ChinaLiedPeopleDied - @SolomonYue @GO… | 2020-04-06T10:28:53.000Z | \["BoycottChina", "ChinaLiedPeopleDied", "MakeChinaPay"\] | 1247109014694932481 | TomaszTrembowsk |


