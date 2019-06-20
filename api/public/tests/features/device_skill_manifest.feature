Feature: Device can upload and fetch skills manifest

  Scenario: Device retrieves its manifest from the API
    Given an authorized device
    When a device requests its skill manifest
    Then the request will be successful
    And the response will contain the manifest

  Scenario: Device uploads an unchanged manifest
    Given an authorized device
    When a device uploads a skill manifest without changes
    Then the request will be successful
    And the skill manifest on the database is unchanged
    And device last contact timestamp is updated

  Scenario: Device uploads a manifest with an updated skill
    Given an authorized device
    When a device uploads a skill manifest with an updated skill
    Then the request will be successful
    And the skill manifest on the database is unchanged
    And device last contact timestamp is updated

  Scenario: Device uploads a manifest with a deleted skill
    Given an authorized device
    When a device uploads a skill manifest with a deleted skill
    Then the request will be successful
    And the skill is removed from the manifest on the database
    And device last contact timestamp is updated

  @device_specific_skill
  Scenario: Device uploads a manifest with a deleted device-specific skill
    Given an authorized device
    When a device uploads a skill manifest with a deleted device-specific skill
    Then the request will be successful
    And the device-specific skill is removed from the manifest on the database
    And the device-specific skill is removed from the database
    And device last contact timestamp is updated

  @new_skill
  Scenario: Device uploads a manifest with a new skill
    Given an authorized device
    When a device uploads a skill manifest with a new skill
    Then the request will be successful
    And the skill is added to the database
    And the skill is added to the manifest on the database
    And device last contact timestamp is updated

