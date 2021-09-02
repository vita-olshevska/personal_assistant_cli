# **Personal\_assistant\_cli**

Personal assistant cli - is a bot, which has the next main functionalities:

- records managing
- notes managing
- sort files/directories

The program is written using Python. It has several packages that are automatically installed (prettytable and fuzzywuzzy). The program also uses a local database to store data.

## 1. Instructions for installing the package.

The package can be found by the link [https://github.com/vita-olshevska/personal\_assistant\_cli/](https://github.com/vita-olshevska/personal_assistant_cli/) .
It can be installed as the Python package from the console with command &quot;pip3 install .&quot;. It starts with the command &quot;personal\_assistant\_cli&quot; .

## 2. Use and commands:

The single command of bot can be launched by user input, which has two mods:

- direct input - the bot clarifies the user request by multiple questions;

- input in a single line - the bot automatically parses the user request.

Note that, the bot chooses the input mod automatically based on the user request.

**Input requirements:**
   phone number, email and birthday do not contain spaces inside.

**Description of commands:**

| **AddressBook commands:** |
| --- |:---   |
| show records | show all records for AddressBook |
| add record | add the record (phone, address, email or birthday) to the AddressBook |
| change record | change some record (phone, address, email or birthday) |
| delete record | delete the whole record by its name |
| search record | searches for matches for records |
| show birthdays | searches for everyone who has a birthday during stated number of days, starting from today |
| **Or input in 1 line** for AddressBook: |
| \&lt;command\&gt; \&lt;name\&gt; \&lt;your information\&gt;1. you haven`t write your information for command &quot;delete record&quot;;2. you haven&#39;t write a name for commands: &quot;search record&quot; and &quot;search birthdays&quot;.e.g. \&gt;\&gt;\&gt; delete record Vita\&gt;\&gt;\&gt; search birthdays 56 |

| **NoteBook commands:** |
| --- |
| show notes | show all notes for NoteBook |
| add note | add the note to the NoteBook |
| add tag | add tag to an existing note |
| change note | change the note for its id from the table |
| delete note | delete the whole note by its id |
| search note | searches for matches for notes |
| filter note | searches for matches for tags |
| **Or input in 1 line** for NoteBook: |
| \&lt;command\&gt; \&lt;id\&gt; \&lt;some text\&gt;
1. you haven`t write an id for commands: &quot;add note&quot;, &quot;search note&quot;, &quot;filter note&quot;;
 2. you haven&#39;t write a text for the command &quot;delete note&quot;.e.g. \&gt;\&gt;\&gt; add note Do my homework\&gt;\&gt;\&gt; delete note 4 |

| **SearchManager command:** |
| --- |
| sort \&lt;path\&gt; | sorts all files by folders (music, videos, pictures, documents, archives, other) |

| **Another commands:** |
| --- |
| help | displays a table of commands for each module |
| off | turn off the bot |
