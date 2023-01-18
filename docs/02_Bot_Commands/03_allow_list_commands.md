# Group Allow List Commands

InJobBot can be added into groups and used by the owner or group admin to send jobs in chat or by group chat members *(normal members)* to view help and tips messages. 

However, to prevent the abuse of the bot, it has a table in the database which is created on deployment or activation that has the list of groups id's that the bot is allowed to be added to. 

If the bot was added to a group which is not in the database; it will leave. 

??? abstract "Click to view the ^^==allow_list schema==^^ being created"
    ``` py title="persistence.py" linenums="43" hl_lines="22 23 24 25 26 27 28 29"
    class UsersDatabase(IPersistenceLayer):
        """This class sits between the database commands and the database manger class"""

        def __init__(self) -> None:
            """_summary_ : This creates the 2 tables 'users' and 'allow_list'"""
            # Table name to be created if not existing
            self.table_name = "bot_users"
            # Initiating the data base users
            self.db = DatabaseManger("bot_db.sqlite")

            # Creating the table 'bot_users' in the database
            self.db.create_table(
                self.table_name,
                {
                    # "id": "integer primary key autoincrement",
                    "user_id": "text primary key not null",
                    "block_type": "text not null",
                    "date_added": "text not null",
                },
            )
            # Creating the allowlist table
            self.db.create_table(
                "allow_list",
                {
                    "group_id": "text primary key not null",
                },
            )
    ```

This can be controlled by the bot's owner using the following commands.  

****

## Adding A Group To The List

The `/addgroup` command followed by the group chat id will ^^add^^ the group to the database. This command calls the `execute()` method on the the `AddGroupToAllowListCommand(group_id)` database command; ^^adding^^ the group to the allow_list table.

!!! example ""
    <figure markdown>
    ![ljob_command](../assets/bot_commands/addgroup_command.gif){width="500"}
    <figcaption>/addgroup command.</figcaption>
    </figure>

??? abstract "Click to view the `AddGroupToAllowListCommand()` database command class"
    ::: src.database.db_commands.AddGroupToAllowListCommand

****

## Removing A Group From The List

The `/rmgroup` command followed by the group chat id will ^^remove^^ the group from the database. This command calls the `execute()` method on the the `DeleteGroupCommand(group_id)` database command; ^^removing^^ the group from the allow_list table.

!!! example ""
    <figure markdown>
    ![ljob_command](../assets/bot_commands/rmgroup_command.gif){width="500"}
    <figcaption>/rmgroup command.</figcaption>
    </figure>

??? abstract "Click to view the `DeleteGroupCommand()` database command class"
    ::: src.database.db_commands.DeleteGroupCommand

****

## Getting Groups In The List

The `/getgroups` command will ^^list^^ all the groups in the database. This command calls the `execute()` method on the the `GetGroupCommand(group_id)` database command; ^^listing^^ all the groups in the allow_list table.

!!! note 
    Following the `/getgroups` command by the group chat id; will return the group id back if it exists in the database. 

!!! example ""
    <figure markdown>
    ![ljob_command](../assets/bot_commands/getgroup_command.gif){width="500"}
    <figcaption>/getgroup command.</figcaption>
    </figure>

??? abstract "Click to view the `GetGroupCommand()` database command class"
    ::: src.database.db_commands.GetGroupCommand