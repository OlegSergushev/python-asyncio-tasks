# python-asyncio-tasks
Short Python scripts using asyncio to showcase asynchronous programming concepts.
## What's inside
- 'fireworks_show.py': This script simulates a fireworks show using Python's `asyncio` module.
- 'wood_craft.py': Asynchronous code implements interaction between two coroutines: one that gathers wood and the other that makes items from that wood.
- 'port_scanning.py': The program simulates the execution of asynchronous network requests using `asyncio.sleep()`.
- 'dungeon_exploration.py': The code allows a group of players to enter dungeons. Each dungeon is entered with exactly 5 players. The code forms groups using `asyncio.Barrier`. The `enter_dungeon()` coroutine waits for the time specified for each player, and then queues up to wait using the barrier.
- 'dungeon_exploration_2.py': Improved version of `dungeon_exploration.py` code. The new code takes into account the moment when there will not be enough players to gather a full group for a long time. If any of the players in the queue to enter waits more than 5 seconds, the barrier will be reset.
- 'asynchronous_notifications.py': The program simulates the operation of the notification system.
- 'patient_coordination.py': This is an asynchronous code for distributing patients to specialist doctors in a medical center. The code manages patient queues, where each patient has a referral to a doctor of a certain profile. There are 3 queues in total.
