# Changelog
All notable changes to KoalaBot will be documented in this file.
A lot of these commands will only be available to administrators

## [Unreleased]
### Text Filter
##### Changed
- Add regex validation to ensure valid regex only
- Fix mod channel not saving correctly
- Fix regex incorrectly being used on some messages


## [0.2.0] - 15-10-2020
### Text Filter
##### Added
- `filter <text> [type]`  Filter a word or string of text. Type is defaulted to `banned` which will delete the message and warn the user. Use type `risky` to just warn the user.
- `filterRegex <regex> [type]` Filter a regex string. Type is defaulted to `banned` which will delete the message and warn the user. Use type `risky` to just warn the user.
- `filterList` Get a list of filtered words in the server

- `modChannelAdd <channelId>` Add a mod channel for receiving filtered message information (User, Timestamp, Message) to be sent to.
- `modChannelRemove <channelId>` Remove a mod channel from the server.
- `modChannelList` See a list of mod channels in the server.

- `ignoreUser <userMention>` Add a new ignored user for the server. This users' messages will be ignored by the Text Filter.
- `ignoreChannel <channelMention>` Add a new ignored channel for the server. Messages in this channel will be ignored by the Text Filter.
- `ignoreList` See a list of ignored users/channels in the server.

- `unfilter <text>` Unfilter a word/string/regex of text that was previously filtered.
- `unignore <mention>` Unignore a user/channel that was previously set as ignored

### React For Role (RFR)
##### Added
- `rfr create` Create a new, blank rfr message. Default title is `React for Role`. Default description is `Roles below!`. 
- `rfr delete` Delete an existing rfr message. 
- `rfr addRequiredRole` Add a role required to react to/use rfr functionality. If no role is added, anyone can use rfr functionality.
- `rfr removeRequiredRole` Removes a role from the group of roles someone requires to use rfr functionality 

- `rfr edit addRoles` Add emoji/role combos to an existing rfr message. 
- `rfr edit removeRoles` Remove emoji/role combos from an existing rfr message. 
- `rfr edit description` Edit the description of an existing rfr message  
- `rfr edit title` Edit the title of an existing rfr message.

### Colour Role
##### Changed
- Fixed error that occasionally made custom colour roles be created in the wrong position, thus not showing correctly

### Twitch Alert
##### Changed
- Add catch so errors don't stop the alert loop


## [0.1.8] - 18-10-2020
### Twitch Alert
##### Changed
- Add 'No Category' option
- Reduced Logging
- Fix regex allowing underscore at start of name

## [0.1.7] - 13-10-2020
### Twitch Alert
##### Changed
- Fix InvalidArgument errors from not showing
- Add logging
- Add removal of chats that are no longer accessible

## [0.1.6] - 12-10-2020
### Twitch Alert
##### Changed
- Minor Bug Fixes

## [0.1.5] - 11-10-2020
### Verification
##### Changed
- Fix bot erroring on startup if it had left any guilds with verification enabled
#### Twitch Alert 
##### Changed
- Fix use of full URLs in twitch alerts
- Fix oauth not updating

## [0.1.4] - 10-10-2020
#### Twitch Alert 
##### Changed
- Fix TwitchAlert loops crashing
- Fix repeat on_ready
- Fix timout for requests
- Fix Twitch API Limits followed
- Update TwitchAlert to use aiohttp rather than requests

## [0.1.3] - 30-9-2020
### Verification
##### Changed
- Fixed a bug involving verification of an email matching a server you weren't in

## [0.1.2] - 22-9-2020
### Base KoalaBot
##### Changed
- Fixed bug of k!help not working within a direct message
- Fixed bug of TwitchAlert crashing
- Fixed bug of adding a team to a new channel sets message as the Guild ID
### Verification
##### Changed
- Edited message sent upon joining a server with verification enabled


## [0.1.1] - 19-9-2020
### Koala Extensions
#### Twitch Alert *by [Jack Draper](https://github.com/jaydwee)*
##### Changed
- Fix an issue with not deleting old alerts

## [0.1.0] - 19-9-2020
### Base KoalaBot
##### Added
- `enableExt <koala_extension>` Enable available Koala Extensions
- `disableExt <koala_extension>` Disable enabled Koala Extensions
- `listExt` Lists all enabled and disabled Koala Extensions

* `welcomeUpdateMsg <new_message>` Allows admins to change their customisable part of the welcome message of a guild.
* `welcomeSendMsg` Allows admins to send out their welcome message manually to all members of a guild.
* `welcomeViewMsg` Shows the current welcome message

- `clear [amount=2]` Clears a given number of messages from the given channel
- `ping` Returns the ping of the bot

### Koala Extensions
#### **Verify** *by [Harry Nelson](https://github.com/largereptile)*
##### Added
- `verifyAdd [suffix] [role]` Set up a role and email pair for KoalaBot to verify users with
- `verifyRemove [suffix] [role]` Disable an existing verification listener
- `reVerify <role>` Removes a role from all users who have it and marks them as needing to re-verify before giving it back
- `verifyList` List the current verification setup for the server

#### **Twitch Alert** *by [Jack Draper](https://github.com/jaydwee)*
##### Added
- `twitchEditMsg <channel_id> [default_live_message...]` Edit the default message put in a Twitch Alert Notification
- `twitchViewMsg [channel_id]` Shows the current default message for Twitch Alerts
- `twitchList` Shows all current users and teams in a Twitch Alert
- `twitchAdd <channel_id> [twitch_username] [custom_live_message...]` Add a Twitch user to a Twitch Alert
- `twitchAddTeam <channel_id> [team_name] [custom_live_message...]` Add a Twitch team to a Twitch Alert
- `twitchRemove <channel_id> [twitch_username]`  Removes a user from a Twitch Alert
- `twitchRemoveTeam <channel_id> [team_name]` Removes a team from a Twitch Alert

#### **ColourRole** *by [Anan Venkatesh](https://github.com/Unknownlocal)*
##### Added
- `listCustomColourAllowedRoles` Lists the roles in a guild which are permitted to have their own custom colours.
- `listProtectedRoleColours` Lists the protected roles, whose colours are protected from being imitated by a custom colour, in a guild.
- `addCustomColourAllowedRole <role>` Adds a role, via ID, mention or name, to the list of roles allowed to have a custom colour.
- `addProtectedRoleColour <role_str>` Adds a role, via ID, mention or name, to the list of protected roles.
- `removeCustomColourAllowedRole <role_str>` Removes a role, via ID, mention or name, from the list of roles allowed to have a custom colour.
- `removeProtectedRoleColour <role_str>` Removes a role, via ID, mention or name, from the list of protected roles.

[Unreleased]: https://github.com/KoalaBotUK/KoalaBot/compare/v0.1.0...HEAD
[0.2.0]: https://github.com/KoalaBotUK/KoalaBot/compare/v0.1.8...v0.2.0
[0.1.8]: https://github.com/KoalaBotUK/KoalaBot/compare/v0.1.7...v0.1.8
[0.1.7]: https://github.com/KoalaBotUK/KoalaBot/compare/v0.1.6...v0.1.7
[0.1.6]: https://github.com/KoalaBotUK/KoalaBot/compare/v0.1.5...v0.1.6
[0.1.5]: https://github.com/KoalaBotUK/KoalaBot/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/KoalaBotUK/KoalaBot/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/KoalaBotUK/KoalaBot/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/KoalaBotUK/KoalaBot/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/KoalaBotUK/KoalaBot/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/KoalaBotUK/KoalaBot/releases/tag/v0.1.0
